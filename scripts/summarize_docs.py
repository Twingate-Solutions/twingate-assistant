"""Fetch a Twingate doc page and generate a structured summary via the Claude API."""

import hashlib
import logging
import re

import anthropic
import requests
from bs4 import BeautifulSoup

from url_safety import REQUEST_HEADERS, _is_safe_url

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT_SECONDS = 30
CLAUDE_MODEL = "claude-sonnet-4-6"
CLAUDE_MAX_TOKENS = 1024
MAX_TEXT_LENGTH = 60000

SYSTEM_PROMPT = (
    "You are summarizing a Twingate documentation page for use as a "
    "reference file in a Claude Code plugin. Produce a structured markdown "
    "summary with: Page Title, Summary (2-3 sentences), Key Information "
    "(bullets), Prerequisites, Step-by-Step (if applicable), Configuration "
    "Values (env vars, CLI flags, API params), Gotchas, Related Docs. Keep "
    "under 500 words. Focus on actionable implementation guidance. No "
    "marketing language."
)

# Tags removed entirely before extracting text.
REMOVE_TAGS = ("script", "style", "nav", "footer", "header", "aside")

# CSS selectors tried in order to find the main content area.
MAIN_CONTENT_SELECTORS = ("main", "article", "#content", ".content", ".kb-article-main")

# Footer label lines stripped by ``normalize_for_hash``.
_LAST_UPDATED_LABEL = "last updated"
_OPEN_WITH_AI_LABEL = "open with ai"
# Matches a "N units ago" relative-age line.
_RELATIVE_AGE_RE = re.compile(
    r"^(?:just now|yesterday|"
    r"(?:a|an|\d+)\s+(?:second|minute|hour|day|week|month|year)s?\s+ago)$",
    re.IGNORECASE,
)


def fetch_doc_html(url: str) -> str | None:
    """Fetch a documentation page and return its HTML.

    Args:
        url: The full URL of the documentation page to fetch.

    Returns:
        The HTML content as a string, or ``None`` if the request failed or
        the URL did not pass the allowlist check.
    """
    if not _is_safe_url(url):
        logger.warning("Refusing to fetch non-twingate URL: %s", url)
        return None
    try:
        logger.info("Fetching doc page: %s", url)
        response = requests.get(url, timeout=REQUEST_TIMEOUT_SECONDS, headers=REQUEST_HEADERS)
        response.raise_for_status()
        logger.info(
            "Fetched %s successfully, status=%d, length=%d bytes",
            url,
            response.status_code,
            len(response.content),
        )
        return response.text
    except requests.RequestException as exc:
        logger.warning("Failed to fetch %s: %s", url, exc)
        return None


def extract_text_from_html(html_content: str) -> str:
    """Extract readable text from HTML, stripping boilerplate elements.

    Falls back to the full ``<body>`` or the entire document if no main
    content container is found.

    Args:
        html_content: Raw HTML string to process.

    Returns:
        Plain text extracted from the HTML with normalized whitespace.
    """
    soup = BeautifulSoup(html_content, "lxml")

    for tag_name in REMOVE_TAGS:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    content_element = None
    for selector in MAIN_CONTENT_SELECTORS:
        content_element = soup.select_one(selector)
        if content_element is not None:
            break

    if content_element is None:
        content_element = soup.body if soup.body else soup

    text = content_element.get_text(separator="\n", strip=True)
    return text


def content_hash(text: str) -> str:
    """Compute a SHA-256 hex digest of the given text.

    Args:
        text: The text string to hash.

    Returns:
        A 64-character lowercase hexadecimal SHA-256 digest string.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_for_hash(text: str) -> str:
    """Strip the time-varying "Last updated … ago" footer lines from the text.

    Removes a ``"Last updated"`` line together with an immediately following
    relative-age line, and any standalone ``"Open with AI"`` line. All other
    lines are preserved byte-for-byte.

    Args:
        text: Extracted page text, as returned by ``extract_text_from_html``.

    Returns:
        The text with the footer lines removed, rejoined with ``"\\n"``.
    """
    lines = text.split("\n")
    kept: list[str] = []
    i = 0
    total = len(lines)
    while i < total:
        line = lines[i]
        lowered = line.strip().lower()
        if lowered == _LAST_UPDATED_LABEL:
            # Drop the label, plus the next line if it is a relative-age timestamp.
            if i + 1 < total and _RELATIVE_AGE_RE.match(lines[i + 1].strip()):
                i += 2
            else:
                i += 1
            continue
        if lowered == _OPEN_WITH_AI_LABEL:
            i += 1
            continue
        kept.append(line)
        i += 1
    return "\n".join(kept)


def build_frontmatter(source: str, type_: str, fetched: str, source_version: str) -> str:
    """Build a YAML frontmatter block for a generated reference file.

    Args:
        source: Provenance URL of the page the reference was generated from.
        type_: Source category — ``"docs"``, ``"help"``, or ``"github"``.
        fetched: Date the source was fetched, as an ISO ``YYYY-MM-DD`` string.
        source_version: Version identifier of the source content — a content
            hash for ``docs``/``help`` or a git commit SHA for ``github``.

    Returns:
        A YAML frontmatter block as a string, fenced by ``---`` and ending
        with a newline.
    """
    return (
        "---\n"
        f"source: {source}\n"
        f"type: {type_}\n"
        f"fetched: {fetched}\n"
        f"source_version: {source_version}\n"
        "---\n"
    )


def summarize_doc(url: str, html_content: str) -> str:
    """Call the Claude API to summarize a doc page.

    Requires the ``ANTHROPIC_API_KEY`` environment variable.

    Args:
        url: The source URL of the doc page (included in the prompt).
        html_content: Raw HTML content of the page.

    Returns:
        A structured markdown summary produced by Claude.

    Raises:
        anthropic.APIError: If the Claude API call fails.
        ValueError: If the API response does not contain a text block.
    """
    page_text = extract_text_from_html(html_content)

    if len(page_text) > MAX_TEXT_LENGTH:
        logger.info(
            "Truncating text for %s from %d to %d chars",
            url,
            len(page_text),
            MAX_TEXT_LENGTH,
        )
        page_text = page_text[:MAX_TEXT_LENGTH] + "\n\n[Content truncated for length]"

    user_message = f"URL: {url}\n\n{page_text}"

    logger.info("Calling Claude API for %s (text length=%d)", url, len(page_text))
    client = anthropic.Anthropic()
    message = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=CLAUDE_MAX_TOKENS,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_message}],
    )

    first_block = message.content[0]
    if not hasattr(first_block, "text") or first_block.text is None:
        raise ValueError(
            f"Unexpected content block type from Claude API: {type(first_block)}"
        )
    summary: str = first_block.text
    logger.info("Summary generated for %s (%d chars)", url, len(summary))
    return summary


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )

    import sys

    if len(sys.argv) < 2:
        print("Usage: python summarize_docs.py <url>")
        print("  Fetches the URL, extracts text, and prints a Claude summary.")
        sys.exit(1)

    target_url = sys.argv[1]
    html = fetch_doc_html(target_url)
    if html is None:
        print(f"Failed to fetch {target_url}")
        sys.exit(1)

    text = extract_text_from_html(html)
    print(f"Extracted {len(text)} chars of text")
    print(f"Content hash: {content_hash(text)}")
    print()

    result = summarize_doc(target_url, html)
    print(result)
