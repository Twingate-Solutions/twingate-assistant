"""Structural checks and link maintenance for generated reference files.

Two zero-LLM helpers used by ``update_references``:

* :func:`find_truncation` spots a summary that stops mid-output (an unclosed
  markdown link or code fence). New summaries that fail it are rejected, and
  existing references that fail it are re-summarized.
* :func:`repair_twingate_links` checks every Twingate docs/help link in a
  reference body against the URLs known live this run (sitemaps plus mapped
  pages). A renamed page is rewritten through the ``link_aliases`` table in
  ``doc_mapping.yaml``. Anything else is probed over HTTP: a redirect into a
  live page is rewritten to it, any other success is kept, and only a
  404/410 markdown link is reduced to its text. Probe errors keep the link.
"""

import logging
import re
from collections.abc import Callable, Iterable, Mapping
from dataclasses import dataclass, field
from pathlib import Path
from typing import Literal

import requests

logger = logging.getLogger(__name__)

ProbeStatus = Literal["live", "dead", "unknown"]
# A probe returns the status and, for "live", the canonical final URL.
Probe = Callable[[str], tuple[ProbeStatus, str | None]]

PROBE_TIMEOUT_SECONDS = 15
_PROBE_HEADERS = {"User-Agent": "twingate-assistant-reference-pipeline"}

# Hosts whose pages the pipeline's sitemaps enumerate. ``docs.twingate.com``
# redirects to ``www.twingate.com/docs`` and is checked as that host.
_TWINGATE_URL_RE = re.compile(
    r"https://(?:www\.twingate\.com/docs|docs\.twingate\.com/docs|help\.twingate\.com/articles)"
    r"/[A-Za-z0-9_.~%-]+(?:/[A-Za-z0-9_.~%-]+)*/?(?:#[A-Za-z0-9_.~%-]*)?"
)
_MARKDOWN_LINK_RE = re.compile(r"\[([^\]\n]*)\]\((" + _TWINGATE_URL_RE.pattern + r")\)")

# Below this many live URLs the sitemap fetch is treated as partial and link
# maintenance is skipped, so a bad fetch can never unlink the corpus.
MIN_LIVE_URLS = 50

MANUAL_REFERENCE_MARKER = "manual-reference: do-not-overwrite"


def canonical_url(url: str) -> str:
    """Return ``url`` without its fragment or trailing slash, on the www docs host.

    Args:
        url: A Twingate docs or help-center URL.

    Returns:
        The URL used for sitemap and alias lookups.
    """
    base = url.split("#", 1)[0].rstrip("/")
    return base.replace("https://docs.twingate.com/docs/", "https://www.twingate.com/docs/", 1)


def http_probe(url: str) -> tuple[ProbeStatus, str | None]:
    """Check ``url`` over HTTP, following redirects.

    Args:
        url: A Twingate docs or help-center URL.

    Returns:
        ``("live", final_canonical_url)`` for a 2xx, ``("dead", None)`` for a
        404 or 410, and ``("unknown", None)`` for anything else, including
        network errors.
    """
    try:
        resp = requests.head(
            url, allow_redirects=True, timeout=PROBE_TIMEOUT_SECONDS, headers=_PROBE_HEADERS
        )
        if resp.status_code in (403, 405):
            resp = requests.get(
                url, allow_redirects=True, timeout=PROBE_TIMEOUT_SECONDS, headers=_PROBE_HEADERS
            )
    except requests.RequestException as exc:
        logger.warning("Link probe failed for %s: %s", url, exc)
        return "unknown", None
    if 200 <= resp.status_code < 300:
        return "live", canonical_url(resp.url)
    if resp.status_code in (404, 410):
        return "dead", None
    return "unknown", None


def find_truncation(text: str) -> str | None:
    """Return why ``text`` looks cut off mid-output, or ``None`` if it looks whole.

    Checks for an unclosed code fence anywhere, and for an unclosed markdown
    link or bracket on the last non-empty line.

    Args:
        text: A summary body (frontmatter already removed).

    Returns:
        A short reason string, or ``None``.
    """
    stripped = text.rstrip()
    if not stripped:
        return None
    if stripped.count("```") % 2:
        return "unclosed code fence"
    last = stripped.splitlines()[-1]
    open_link = last.rfind("](")
    if open_link != -1 and ")" not in last[open_link + 2 :]:
        return "unclosed markdown link on the last line"
    if last.count("[") > last.count("]"):
        return "unclosed bracket on the last line"
    return None


@dataclass
class LinkRepairResult:
    """What :func:`repair_twingate_links` changed in one body."""

    text: str
    rewritten: list[tuple[str, str]] = field(default_factory=list)
    unlinked: list[str] = field(default_factory=list)
    unresolved: list[str] = field(default_factory=list)

    @property
    def changed(self) -> bool:
        """Whether the body text was modified."""
        return bool(self.rewritten or self.unlinked)


def repair_twingate_links(
    text: str,
    live_urls: Iterable[str],
    aliases: Mapping[str, str],
    probe: Probe | None = None,
    probe_cache: dict[str, tuple[ProbeStatus, str | None]] | None = None,
) -> LinkRepairResult:
    """Rewrite or unlink Twingate docs/help links that are not known live.

    For each link whose canonical URL is not in ``live_urls``: an ``aliases``
    entry pointing at a live URL rewrites it (keeping any ``#fragment``).
    Otherwise ``probe`` decides: live and redirected to a live URL rewrites to
    that URL; live otherwise keeps the link; dead turns a markdown link into
    its plain text (a dead bare URL is left and reported in ``unresolved``);
    unknown keeps the link. With no ``probe``, such links are kept.

    Args:
        text: A reference body (frontmatter already removed).
        live_urls: Canonical URLs known live this run.
        aliases: Old canonical URL to replacement URL (``link_aliases``).
        probe: Checks a URL not otherwise known; ``None`` keeps it unchecked.
        probe_cache: Per-run cache of probe results, keyed by canonical URL.

    Returns:
        A :class:`LinkRepairResult` with the new text and what changed.
    """
    live = {canonical_url(u) for u in live_urls}
    alias_map = {canonical_url(k): canonical_url(v) for k, v in aliases.items()}
    cache = probe_cache if probe_cache is not None else {}
    result = LinkRepairResult(text=text)

    def _with_fragment(target: str, url: str) -> str:
        return target + ("#" + url.split("#", 1)[1] if "#" in url else "")

    def _replacement(url: str) -> str | None:
        """Return the URL to use for ``url`` (possibly itself), or ``None`` if dead."""
        canon = canonical_url(url)
        if canon in live:
            return url
        target = alias_map.get(canon)
        if target and target in live:
            return _with_fragment(target, url)
        if probe is None:
            return url
        if canon not in cache:
            cache[canon] = probe(canon)
        status, final = cache[canon]
        if status == "dead":
            return None
        if status == "live" and final and final != canon and final in live:
            return _with_fragment(final, url)
        return url

    def _fix_markdown(match: re.Match[str]) -> str:
        label, url = match.group(1), match.group(2)
        new = _replacement(url)
        if new == url:
            return match.group(0)
        if new is not None:
            result.rewritten.append((url, new))
            return f"[{label}]({new})"
        result.unlinked.append(url)
        return label

    out = _MARKDOWN_LINK_RE.sub(_fix_markdown, text)

    def _fix_bare(match: re.Match[str]) -> str:
        url = match.group(0)
        start = match.start()
        if start >= 2 and out[start - 2 : start] == "](":
            return url  # still inside a markdown link that resolved
        new = _replacement(url)
        if new == url:
            return url
        if new is not None:
            result.rewritten.append((url, new))
            return new
        result.unresolved.append(url)
        return url

    result.text = _TWINGATE_URL_RE.sub(_fix_bare, out)
    return result


def split_frontmatter(content: str) -> tuple[str, str]:
    """Split ``content`` into its frontmatter block (with fences) and body.

    Args:
        content: Full reference file text.

    Returns:
        ``(frontmatter, body)``; ``frontmatter`` is ``""`` when absent.
    """
    if content.startswith("---\n"):
        end = content.find("\n---\n", 4)
        if end != -1:
            return content[: end + 5], content[end + 5 :]
    return "", content


def is_truncated_reference(path: Path) -> str | None:
    """Return why the generated reference at ``path`` looks truncated, if it does.

    Hand-authored references and missing or unreadable files return ``None``.

    Args:
        path: Path to a reference file.

    Returns:
        A reason string, or ``None``.
    """
    try:
        content = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if MANUAL_REFERENCE_MARKER in content[:1024]:
        return None
    return find_truncation(split_frontmatter(content)[1])


def repair_reference_tree(
    skills_dir: Path,
    live_urls: Iterable[str],
    aliases: Mapping[str, str],
    probe: Probe | None = http_probe,
) -> dict[str, int]:
    """Repair Twingate links in every generated reference under ``skills_dir``.

    Scans ``skills_dir/*/references/*.md``. Frontmatter is never modified, so
    a file's ``source:`` URL stays as recorded. Hand-authored references are
    skipped. Does nothing when ``live_urls`` has fewer than
    :data:`MIN_LIVE_URLS` entries.

    Args:
        skills_dir: The plugin's ``skills/`` directory.
        live_urls: URLs known live this run: sitemap URLs (after exclusions)
            plus the URLs mapped in ``doc_mapping.yaml``.
        aliases: The ``link_aliases`` table from ``doc_mapping.yaml``.
        probe: Checks URLs not otherwise known (default :func:`http_probe`).

    Returns:
        Counts: ``files_changed``, ``rewritten``, ``unlinked``, ``unresolved``.
    """
    live = {canonical_url(u) for u in live_urls}
    counts = {"files_changed": 0, "rewritten": 0, "unlinked": 0, "unresolved": 0}
    if len(live) < MIN_LIVE_URLS:
        logger.warning(
            "Link maintenance skipped: only %d live URL(s) from sitemaps (minimum %d)",
            len(live),
            MIN_LIVE_URLS,
        )
        return counts

    probe_cache: dict[str, tuple[ProbeStatus, str | None]] = {}
    for path in sorted(skills_dir.glob("*/references/*.md")):
        try:
            content = path.read_text(encoding="utf-8")
        except OSError as exc:
            logger.warning("Link maintenance: could not read %s: %s", path, exc)
            continue
        if MANUAL_REFERENCE_MARKER in content[:1024]:
            continue
        frontmatter, body = split_frontmatter(content)
        repaired = repair_twingate_links(body, live, aliases, probe, probe_cache)
        counts["rewritten"] += len(repaired.rewritten)
        counts["unlinked"] += len(repaired.unlinked)
        counts["unresolved"] += len(repaired.unresolved)
        for url in repaired.unresolved:
            logger.warning("Link maintenance: %s has a dead bare URL with no alias: %s", path, url)
        if repaired.changed:
            path.write_text(frontmatter + repaired.text, encoding="utf-8")
            counts["files_changed"] += 1
            logger.info(
                "Link maintenance: %s — %d rewritten, %d unlinked",
                path,
                len(repaired.rewritten),
                len(repaired.unlinked),
            )
    return counts
