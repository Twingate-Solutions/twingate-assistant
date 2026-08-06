"""LLM-based summarization of Twingate GitHub repositories and wikis."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, cast

import anthropic

from summarize_docs import CLAUDE_MAX_TOKENS, CLAUDE_MODEL, MAX_TEXT_LENGTH

logger = logging.getLogger(__name__)

# Diff file count above which a full re-summarize is used instead of a delta.
MAX_DELTA_FILES = 30

_DELTA_SYSTEM_PROMPT = (
    "You maintain a reference summary for a Twingate GitHub repository. "
    "Here is the current summary and the changes since it was written. "
    "Return an updated summary in the same structure. Preserve accurate "
    "detail; revise only what the changes affect. No marketing language."
)

_FULL_SYSTEM_PROMPT = (
    "Produce a reference summary for this Twingate GitHub repo in the "
    "standard structure: Repo Title, Summary (2-3 sentences), Key "
    "Information (bullets), Prerequisites, Usage / Step-by-Step (if "
    "applicable), Configuration Values (env vars, CLI flags, API params), "
    "Gotchas, Related Docs. Keep under 500 words. No marketing language."
)


@dataclass(frozen=True)
class SummaryResult:
    """The text output of one summarization call, plus its token usage."""

    text: str
    input_tokens: int
    output_tokens: int
    model: str


def _extract_text(message: Any) -> str:
    """Extract the first content block's text.

    Args:
        message: The ``anthropic`` ``Message`` returned by ``messages.create()``.

    Returns:
        The text of the first content block.

    Raises:
        ValueError: If the first content block has no ``text`` attribute.
    """
    first_block = message.content[0]
    if not hasattr(first_block, "text") or first_block.text is None:
        raise ValueError(
            f"Unexpected content block type from Claude API: {type(first_block)}"
        )
    return cast(str, first_block.text)


def _format_metadata(metadata: dict[str, Any]) -> str:
    """Render a repo metadata dict as a short text block for the prompt.

    Args:
        metadata: A dict that may carry ``full_name``, ``description``,
            ``default_branch``, and ``latest_release_notes``.

    Returns:
        A short, human-readable metadata block.
    """
    lines = ["Repo metadata:"]
    name = metadata.get("full_name")
    if name:
        lines.append(f"- Name: {name}")
    description = metadata.get("description")
    if description:
        lines.append(f"- Description: {description}")
    default_branch = metadata.get("default_branch")
    if default_branch:
        lines.append(f"- Default branch: {default_branch}")
    release_notes = metadata.get("latest_release_notes")
    if release_notes:
        lines.append(f"- Latest release notes:\n{release_notes}")
    return "\n".join(lines)


def _assemble_full_corpus(readme: str, key_docs: list[str], *, label: str) -> str:
    """Assemble README + docs markdown into one corpus, truncated to length.

    Args:
        readme: The repo's README text (may be empty).
        key_docs: Additional ``docs/**`` markdown file contents to include.
        label: A human-readable identifier for the repo/wiki.

    Returns:
        The assembled corpus, truncated to ``MAX_TEXT_LENGTH`` characters
        if necessary.
    """
    parts: list[str] = []
    if readme:
        parts.append(f"# README\n\n{readme}")
    for index, doc_text in enumerate(key_docs, start=1):
        parts.append(f"# docs file {index}\n\n{doc_text}")

    corpus = "\n\n---\n\n".join(parts)
    if len(corpus) > MAX_TEXT_LENGTH:
        logger.info(
            "Truncating assembled corpus for %s from %d to %d chars",
            label,
            len(corpus),
            MAX_TEXT_LENGTH,
        )
        corpus = corpus[:MAX_TEXT_LENGTH] + "\n\n[Content truncated for length]"
    return corpus


def summarize_repo_delta(prior_doc: str, filtered_diff: str, metadata: dict[str, Any]) -> SummaryResult:
    """Update an existing repo reference summary from a filtered diff.

    Args:
        prior_doc: The existing reference summary's body (frontmatter stripped).
        filtered_diff: The doc-relevant patch text since ``prior_doc`` was written.
        metadata: Repo metadata dict.

    Returns:
        A ``SummaryResult`` with the updated summary text and token usage.

    Raises:
        anthropic.APIError: Propagated from the API call.
        ValueError: If the API response has an unexpected shape.
    """
    user_message = (
        f"{_format_metadata(metadata)}\n\n"
        f"--- Current summary ---\n{prior_doc}\n\n"
        f"--- Changes since last summary ---\n{filtered_diff}\n"
    )
    logger.info(
        "Calling Claude API for delta summary of %s (diff length=%d)",
        metadata.get("full_name", "unknown"),
        len(filtered_diff),
    )
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=CLAUDE_MAX_TOKENS,
        system=_DELTA_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    text = _extract_text(message)
    return SummaryResult(
        text=text,
        input_tokens=message.usage.input_tokens,
        output_tokens=message.usage.output_tokens,
        model=CLAUDE_MODEL,
    )


def summarize_repo_full(readme: str, key_docs: list[str], metadata: dict[str, Any]) -> SummaryResult:
    """Produce a fresh repo reference summary from README + key docs.

    Args:
        readme: The repo's README text (may be empty).
        key_docs: Additional ``docs/**`` markdown file contents to include.
        metadata: Repo metadata dict.

    Returns:
        A ``SummaryResult`` with the new summary text and token usage.

    Raises:
        anthropic.APIError: Propagated from the API call.
        ValueError: If the API response has an unexpected shape.
    """
    label = str(metadata.get("full_name", "unknown"))
    corpus = _assemble_full_corpus(readme, key_docs, label=label)
    user_message = f"{_format_metadata(metadata)}\n\n{corpus}"

    logger.info("Calling Claude API for full summary of %s (corpus length=%d)", label, len(corpus))
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=CLAUDE_MAX_TOKENS,
        system=_FULL_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )
    text = _extract_text(message)
    return SummaryResult(
        text=text,
        input_tokens=message.usage.input_tokens,
        output_tokens=message.usage.output_tokens,
        model=CLAUDE_MODEL,
    )


def build_metrics_record(
    *,
    full_name: str,
    mode: str,
    result: SummaryResult | None,
    wall_clock_s: float,
    diff_bytes: int,
) -> dict[str, object]:
    """Build one per-repo metrics record.

    Args:
        full_name: The repo's ``{org}/{repo}`` full name.
        mode: One of ``"delta"``, ``"full"``, ``"stub"``, or ``"wiki"``.
        result: The ``SummaryResult`` from the LLM call, or ``None`` when no
            call was made or the call failed.
        wall_clock_s: Wall-clock seconds spent processing this repo/wiki.
        diff_bytes: Byte length of the filtered diff built for this repo/wiki.

    Returns:
        A JSON-serializable record dict.
    """
    return {
        "full_name": full_name,
        "mode": mode,
        "input_tokens": result.input_tokens if result is not None else 0,
        "output_tokens": result.output_tokens if result is not None else 0,
        "wall_clock_s": round(wall_clock_s, 3),
        "diff_bytes": diff_bytes,
    }
