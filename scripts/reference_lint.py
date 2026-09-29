"""Static content scanning for generated reference summaries.

The pipeline feeds scraped, untrusted web/GitHub content to an LLM and writes
its output straight into ``skills/*/references/`` — files a customer's Claude
Code session later reads and may act on. This module is the last line of
defense before that write: a pure scan of the *generated summary text* (not
the raw scrape) for content that would try to redirect an agent reading the
file, or that points a reader at running an untrusted remote script.

Findings carry one of two severities:

- ``BLOCK`` — the text reads as an attempt to reprogram/redirect the agent
  that will later read this reference file (prompt injection). The caller
  must not write the file.
- ``FLAG`` — a pipe-to-shell install pattern, or a link to a host outside the
  known-good allowlist. The caller still writes the file, but records the
  finding for the run's security review report.

Nothing here fetches, writes files, or calls the network — it is a pure
function over a string.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

BLOCK = "BLOCK"
FLAG = "FLAG"

# How much surrounding context to keep in a finding's snippet.
_SNIPPET_MAX_CHARS = 200
_SNIPPET_CONTEXT_BEFORE = 40

# Hostname suffixes considered safe to reference/link from generated content.
# A hostname is allowed if it equals one of these, or ends with "." + one of
# these (so "docs.hashicorp.com" matches "hashicorp.com"). Derived from the
# current skills/*/references/ corpus plus the infra vendors it commonly
# cites for the platforms Twingate connectors and IaC modules run on.
ALLOWED_LINT_HOSTS: frozenset[str] = frozenset(
    {
        "twingate.com",
        "github.com",
        "githubusercontent.com",
        "hashicorp.com",
        "registry.terraform.io",
        "terraform.io",
        "kubernetes.io",
        "helm.sh",
        "docker.com",
        "hub.docker.com",
        "amazonaws.com",
        "aws.amazon.com",
        "microsoft.com",
        "azure.com",
        "google.com",
        "cloud.google.com",
        "googleapis.com",
        "pulumi.com",
        "npmjs.com",
        "pypi.org",
        "python.org",
        "ubuntu.com",
        "debian.org",
        "redhat.com",
        "okta.com",
        "onelogin.com",
        "jumpcloud.com",
        "cloudflare.com",
        "nextdns.io",
    }
)

# Twingate GitHub orgs this pipeline discovers repos/wikis from. Informational
# only — used by callers to annotate a finding's provenance, not by the lint
# rules themselves (see update_references.py's trust-tier frontmatter field).
KNOWN_TWINGATE_ORGS: frozenset[str] = frozenset(
    {"Twingate", "Twingate-Solutions", "Twingate-Labs", "Twingate-Community"}
)

# Twingate's own installer host: the one origin where a pipe-to-shell install
# command is expected and legitimate, so it is exempted from the FLAG below.
_TWINGATE_INSTALLER_HOST = "binaries.twingate.com"


@dataclass(frozen=True)
class LintFinding:
    """One rule match against a generated summary's text."""

    severity: str
    rule: str
    snippet: str


# ---------------------------------------------------------------------------
# BLOCK patterns — prompt injection / agent-directed content.
# ---------------------------------------------------------------------------
#
# Kept deliberately narrow: each pattern requires a directive shape (an
# imperative aimed at "you"/an agent, or a literal control-token-like marker),
# not just a topical word, to avoid tripping on ordinary Twingate docs that
# happen to mention "system", "instructions", or "AI" in passing.

_BLOCK_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "ignore-prior-instructions",
        re.compile(
            r"ignore\s+(?:all\s+|any\s+)?(?:the\s+)?"
            r"(?:previous|prior|above|preceding)\s+instructions",
            re.IGNORECASE,
        ),
    ),
    (
        "disregard-instructions",
        re.compile(
            r"disregard\s+(?:all\s+|any\s+)?(?:the\s+)?"
            r"(?:previous|prior|above|preceding)\s+instructions",
            re.IGNORECASE,
        ),
    ),
    (
        "new-instructions-marker",
        re.compile(r"new\s+instructions\s*:", re.IGNORECASE),
    ),
    (
        "system-prompt-reference",
        re.compile(r"\b(?:the|your)\s+system\s+prompt\b", re.IGNORECASE),
    ),
    (
        "system-tag",
        re.compile(r"</?system>", re.IGNORECASE),
    ),
    (
        "role-reassignment",
        re.compile(
            r"\byou\s+are\s+now\s+(?:a|an|the|acting\s+as|operating\s+as|running\s+as)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "hide-from-user",
        re.compile(r"do\s+not\s+tell\s+the\s+user", re.IGNORECASE),
    ),
    (
        "agent-directive",
        re.compile(
            r"\b(?:claude|assistant)\s*[,:]\s*(?:please\s+)?"
            r"(?:run|execute|delete|download|curl|wget|ignore|disregard)\b",
            re.IGNORECASE,
        ),
    ),
    (
        "ai-directive-aimed-at-reader",
        re.compile(
            r"\bas an ai\b[^.\n]{0,40}\b(?:you (?:must|should|will)|do not)\b",
            re.IGNORECASE,
        ),
    ),
)

# ---------------------------------------------------------------------------
# FLAG patterns — pipe-to-shell installers and disallowed-host links.
# ---------------------------------------------------------------------------

_PIPE_TO_SHELL = re.compile(
    r"\b(?:curl|wget|iwr|invoke-webrequest)\b[^\n|]*\|\s*"
    r"(?:sudo\s+)?(?:bash|sh|zsh|python[23]?|iex|invoke-expression)\b",
    re.IGNORECASE,
)

_BASE64_DECODE_PIPE = re.compile(
    r"base64\s+(?:-d|--decode)\b[^\n|]*\|\s*(?:sudo\s+)?(?:bash|sh|zsh)\b",
    re.IGNORECASE,
)

_EVAL_CURL = re.compile(r"eval\s+[\"']?\$\(\s*curl\b", re.IGNORECASE)

_URL_RE = re.compile(r"https?://[^\s)\]}\"'<>]+")


def _snippet(text: str, start: int, end: int) -> str:
    """Extract a truncated, whitespace-collapsed snippet around a match span.

    Args:
        text: The full text the match was found in.
        start: Match start offset.
        end: Match end offset.

    Returns:
        A snippet of at most ``_SNIPPET_MAX_CHARS`` characters, with
        surrounding whitespace/newlines collapsed to single spaces.
    """
    context_start = max(0, start - _SNIPPET_CONTEXT_BEFORE)
    raw = text[context_start:end]
    collapsed = re.sub(r"\s+", " ", raw).strip()
    if len(collapsed) > _SNIPPET_MAX_CHARS:
        collapsed = collapsed[:_SNIPPET_MAX_CHARS].rstrip() + "…"
    return collapsed


def _hostname_allowed(hostname: str | None) -> bool:
    """Return True if ``hostname`` matches the lint allowlist by suffix.

    Args:
        hostname: A lowercase or mixed-case hostname, or ``None``.

    Returns:
        True if the hostname equals, or is a subdomain of, an entry in
        :data:`ALLOWED_LINT_HOSTS`.
    """
    if not hostname:
        return False
    host = hostname.lower()
    return any(host == allowed or host.endswith(f".{allowed}") for allowed in ALLOWED_LINT_HOSTS)


def _pipe_to_shell_target_is_installer(match_text: str) -> bool:
    """Return True if the only URL host in a pipe-to-shell match is the installer.

    Args:
        match_text: The substring matched by :data:`_PIPE_TO_SHELL`.

    Returns:
        True if a URL is present and every URL host found resolves to
        :data:`_TWINGATE_INSTALLER_HOST`; False otherwise (including when no
        URL is present at all, e.g. a bare ``curl $VAR | sh``).
    """
    urls = _URL_RE.findall(match_text)
    if not urls:
        return False
    hosts = {urlparse(u).hostname or "" for u in urls}
    return hosts == {_TWINGATE_INSTALLER_HOST}


def lint_summary(text: str) -> list[LintFinding]:
    """Scan a generated summary's text and return every rule match.

    Pure function: no I/O, no network, no mutation.

    Args:
        text: The generated markdown summary body to scan.

    Returns:
        A list of :class:`LintFinding`, empty if nothing matched. Order is
        not significant to callers, but is stable (BLOCK rules, then FLAG
        rules, in declaration order, then disallowed-host URLs).
    """
    findings: list[LintFinding] = []

    for rule, pattern in _BLOCK_PATTERNS:
        for match in pattern.finditer(text):
            findings.append(
                LintFinding(
                    severity=BLOCK,
                    rule=rule,
                    snippet=_snippet(text, match.start(), match.end()),
                )
            )

    for match in _PIPE_TO_SHELL.finditer(text):
        if _pipe_to_shell_target_is_installer(match.group(0)):
            continue
        findings.append(
            LintFinding(
                severity=FLAG,
                rule="pipe-to-shell",
                snippet=_snippet(text, match.start(), match.end()),
            )
        )

    for match in _BASE64_DECODE_PIPE.finditer(text):
        findings.append(
            LintFinding(
                severity=FLAG,
                rule="base64-decode-pipe-to-shell",
                snippet=_snippet(text, match.start(), match.end()),
            )
        )

    for match in _EVAL_CURL.finditer(text):
        findings.append(
            LintFinding(
                severity=FLAG,
                rule="eval-curl-substitution",
                snippet=_snippet(text, match.start(), match.end()),
            )
        )

    for match in _URL_RE.finditer(text):
        hostname = urlparse(match.group(0)).hostname
        if not _hostname_allowed(hostname):
            findings.append(
                LintFinding(
                    severity=FLAG,
                    rule="disallowed-host-url",
                    snippet=_snippet(text, match.start(), match.end()),
                )
            )

    return findings


@dataclass
class SecurityFinding:
    """One recorded lint finding, with the write it was found while processing."""

    source: str
    target_path: str
    severity: str
    rule: str
    snippet: str


@dataclass
class SecurityReport:
    """Accumulates lint findings across one pipeline run."""

    findings: list[SecurityFinding] = field(default_factory=list)

    def record(self, *, source: str, target_path: str, finding: LintFinding) -> None:
        """Append one finding to the run's accumulated report.

        Args:
            source: Provenance URL of the content that was scanned.
            target_path: The reference file path the content would be (or
                was) written to.
            finding: The :class:`LintFinding` to record.
        """
        self.findings.append(
            SecurityFinding(
                source=source,
                target_path=target_path,
                severity=finding.severity,
                rule=finding.rule,
                snippet=finding.snippet,
            )
        )

    @property
    def block_count(self) -> int:
        """Number of BLOCK-severity findings recorded so far."""
        return sum(1 for f in self.findings if f.severity == BLOCK)

    @property
    def flag_count(self) -> int:
        """Number of FLAG-severity findings recorded so far."""
        return sum(1 for f in self.findings if f.severity == FLAG)

    @property
    def has_findings(self) -> bool:
        """True if any BLOCK or FLAG finding was recorded."""
        return bool(self.findings)


def lint_and_record(
    content: str,
    *,
    source: str,
    target_path: Path,
    security: SecurityReport | None,
) -> bool:
    """Lint generated summary content and record any findings.

    Call this before writing generated content to a reference file. A
    ``security`` accumulator, when given, receives every finding (BLOCK and
    FLAG alike) so the run's security review report is complete regardless
    of the outcome.

    Args:
        content: The generated summary text to scan.
        source: Provenance URL of the content (for the report).
        target_path: The path the content would be written to (for the
            report and for log messages).
        security: The run's :class:`SecurityReport` accumulator, or ``None``
            to skip recording (findings are still logged).

    Returns:
        True if ``content`` contains no BLOCK-severity finding and may be
        written; False if the caller must not write it.
    """
    findings = lint_summary(content)
    blocked = False
    for finding in findings:
        if security is not None:
            security.record(source=source, target_path=str(target_path), finding=finding)
        if finding.severity == BLOCK:
            blocked = True
            logger.error(
                "BLOCKED write to %s: rule=%s source=%s snippet=%r",
                target_path,
                finding.rule,
                source,
                finding.snippet,
            )
        else:
            logger.warning(
                "FLAGGED content for %s: rule=%s source=%s snippet=%r",
                target_path,
                finding.rule,
                source,
                finding.snippet,
            )
    return not blocked


def write_markdown_report(report: SecurityReport, path: Path) -> None:
    """Write the run's accumulated lint findings as a markdown report.

    Always writes a report, even with zero findings (states "No flagged
    content" in that case), so a scheduled job can unconditionally attach it.

    Args:
        report: The run's accumulated :class:`SecurityReport`.
        path: Destination file path; parent directories are created.
    """
    lines = ["# Security Review Report", ""]
    if not report.findings:
        lines.append("No flagged content.")
    else:
        lines.append(
            f"{report.block_count} BLOCK finding(s), {report.flag_count} FLAG finding(s)."
        )
        lines.append("")
        lines.append("| Severity | Rule | Source | Target | Snippet |")
        lines.append("|---|---|---|---|---|")
        for finding in report.findings:
            snippet = finding.snippet.replace("|", "\\|").replace("\n", " ")
            source = finding.source.replace("|", "\\|")
            target = finding.target_path.replace("|", "\\|")
            lines.append(
                f"| {finding.severity} | {finding.rule} | {source} | {target} | {snippet} |"
            )

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")
