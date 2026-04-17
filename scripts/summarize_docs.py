"""Fetch doc pages and generate structured summaries via Claude API.

This module fetches a Twingate documentation page's HTML, strips it
down to plain text, and calls the Claude API (Sonnet) to produce a
structured markdown summary suitable for inclusion as a reference file
in the Claude Code plugin. Used by the auto-update pipeline.
"""

import hashlib
import logging

import anthropic
import requests
from bs4 import BeautifulSoup

from url_safety import REQUEST_HEADERS, _is_safe_url

logger = logging.getLogger(__name__)

REQUEST_TIMEOUT_SECONDS = 30
CLAUDE_MODEL = "claude-sonnet-4-6"
CLAUDE_MAX_TOKENS = 1024
MAX_TEXT_LENGTH = 8000

SYSTEM_PROMPT = (
    "You are summarizing a Twingate documentation page for use as a "
    "reference file in a Claude Code plugin. Produce a structured markdown "
    "summary with: Page Title, Summary (2-3 sentences), Key Information "
    "(bullets), Prerequisites, Step-by-Step (if applicable), Configuration "
    "Values (env vars, CLI flags, API params), Gotchas, Related Docs. Keep "
    "under 500 words. Focus on actionable implementation guidance. No "
    "marketing language."
)

# Tags that should be removed entirely before extracting text.
REMOVE_TAGS = ("script", "style", "nav", "footer", "header", "aside")

# CSS selectors tried in order to find the main content area.
MAIN_CONTENT_SELECTORS = ("main", "article", "#content", ".content")


def fetch_doc_html(url: str) -> str | None:
    """Fetch a documentation page and return its HTML.

    Validates that the URL points to www.twingate.com over HTTPS before
    fetching. Makes an HTTP GET request and returns the response body as
    a string. Returns ``None`` on any request failure (network error,
    timeout, non-2xx status, or disallowed URL) and logs a warning
    instead of raising.

    Args:
        url: The full URL of the documentation page to fetch.

    Returns:
        The HTML content as a string, or ``None`` if the request failed
        or the URL did not pass domain/scheme validation.
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

    Parses the HTML with BeautifulSoup (lxml parser), removes script,
    style, navigation, and other non-content tags, then attempts to
    locate the main content area. Falls back to the full ``<body>`` or
    the entire document if no main content container is found.

    Args:
        html_content: Raw HTML string to process.

    Returns:
        Plain text extracted from the HTML with normalized whitespace.
    """
    soup = BeautifulSoup(html_content, "lxml")

    # Remove non-content tags entirely.
    for tag_name in REMOVE_TAGS:
        for tag in soup.find_all(tag_name):
            tag.decompose()

    # Try to narrow to the main content area.
    content_element = None
    for selector in MAIN_CONTENT_SELECTORS:
        content_element = soup.select_one(selector)
        if content_element is not None:
            break

    # Fall back to <body>, then the whole document.
    if content_element is None:
        content_element = soup.body if soup.body else soup

    text = content_element.get_text(separator="\n", strip=True)
    return text


def content_hash(text: str) -> str:
    """Compute a SHA-256 hex digest of the given text.

    Used for change detection so the pipeline can skip re-summarizing
    pages whose content has not changed since the last run.

    Args:
        text: The text string to hash.

    Returns:
        A 64-character lowercase hexadecimal SHA-256 digest string.
    """
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def summarize_doc(url: str, html_content: str) -> str:
    """Call Claude API (Sonnet) to summarize a doc page.

    Extracts plain text from the HTML, truncates to the maximum allowed
    length, and sends it to the Claude API with a structured summary
    prompt. The ``ANTHROPIC_API_KEY`` environment variable must be set.

    Args:
        url: The source URL of the doc page (included in the prompt
            for context).
        html_content: Raw HTML content of the page.

    Returns:
        A structured markdown summary produced by Claude.

    Raises:
        anthropic.APIError: If the Claude API call fails. The caller
            is responsible for retry logic.
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
