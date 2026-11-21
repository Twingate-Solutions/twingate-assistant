"""Tests for reference_links: truncation detection and Twingate link maintenance."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from reference_links import (
    MIN_LIVE_URLS,
    canonical_url,
    find_truncation,
    http_probe,
    is_truncated_reference,
    repair_reference_tree,
    repair_twingate_links,
)

D = "https://www.twingate.com/docs/"
LIVE = {D + "connectors", D + "clients", D + "privileged-access-management"}


def _live_many() -> set[str]:
    """A live set large enough to clear MIN_LIVE_URLS."""
    return LIVE | {f"{D}page-{i}" for i in range(MIN_LIVE_URLS)}


# ── find_truncation ──────────────────────────────────────────────────────────


@pytest.mark.parametrize(
    "text",
    [
        "# Title\n\n## Related Docs\n- [Connectors](https://www.twingate.com/docs/connectors)\n",
        "# Title\n\nPlain closing sentence.",
        "```yaml\na: 1\n```\nDone.",
        "",
    ],
)
def test_find_truncation_accepts_complete_text(text):
    assert find_truncation(text) is None


@pytest.mark.parametrize(
    ("text", "reason"),
    [
        ("## Related Docs\n- [Peer-to-Peer](https://www.t", "unclosed markdown link"),
        ("## Related Docs\n- [Configuration](documentation/", "unclosed markdown link"),
        ("## Related Docs\n- [Manage Chrome user profiles", "unclosed bracket"),
        ("```bash\necho hi\n", "unclosed code fence"),
    ],
)
def test_find_truncation_flags_cut_off_text(text, reason):
    assert reason in (find_truncation(text) or "")


def test_is_truncated_reference_ignores_frontmatter_and_manual_files(tmp_path):
    generated = tmp_path / "gen.md"
    generated.write_text("---\nsource: x\n---\n\n# T\n- [Docs](https://www.tw", encoding="utf-8")
    manual = tmp_path / "manual.md"
    manual.write_text("<!-- manual-reference: do-not-overwrite -->\n- [Docs](https://www.tw", encoding="utf-8")
    assert is_truncated_reference(generated)
    assert is_truncated_reference(manual) is None
    assert is_truncated_reference(tmp_path / "missing.md") is None


# ── canonical_url ────────────────────────────────────────────────────────────


def test_canonical_url_strips_fragment_slash_and_normalizes_docs_host():
    assert canonical_url(D + "connectors/#ha") == D + "connectors"
    assert canonical_url("https://docs.twingate.com/docs/connectors") == D + "connectors"


# ── repair_twingate_links ────────────────────────────────────────────────────


def test_live_links_and_non_twingate_links_are_untouched():
    text = f"- [C]({D}connectors)\n- [GH](https://github.com/Twingate/gateway)\n"
    result = repair_twingate_links(text, LIVE, {}, probe=MagicMock())
    assert result.text == text
    assert not result.changed


def test_alias_rewrites_markdown_and_bare_urls_keeping_fragment():
    aliases = {D + "identity-firewall": D + "privileged-access-management", D + "client": D + "clients"}
    text = f"- [Overview]({D}identity-firewall#ssh)\nSee {D}client for more.\n"
    result = repair_twingate_links(text, LIVE, aliases)
    assert result.text == (
        f"- [Overview]({D}privileged-access-management#ssh)\nSee {D}clients for more.\n"
    )
    assert len(result.rewritten) == 2


def test_alias_to_a_url_that_is_not_live_is_ignored():
    probe = MagicMock(return_value=("unknown", None))
    result = repair_twingate_links(f"[X]({D}old)", LIVE, {D + "old": D + "also-gone"}, probe=probe)
    assert result.text == f"[X]({D}old)"


def test_dead_markdown_link_becomes_its_text_and_dead_bare_url_is_reported():
    probe = MagicMock(return_value=("dead", None))
    text = f"- [Fair Use Policy]({D}fair-use-policy)\nBare: {D}gone-page\n"
    result = repair_twingate_links(text, LIVE, {}, probe=probe)
    assert result.text == f"- Fair Use Policy\nBare: {D}gone-page\n"
    assert result.unlinked == [D + "fair-use-policy"]
    assert result.unresolved == [D + "gone-page"]


def test_redirect_into_a_live_page_rewrites_to_the_target():
    probe = MagicMock(return_value=("live", D + "clients"))
    result = repair_twingate_links(f"[Download]({D}download)", LIVE, {}, probe=probe)
    assert result.text == f"[Download]({D}clients)"


def test_live_but_unlisted_and_unknown_probe_results_keep_the_link():
    for status, final in (("live", D + "unlisted-page"), ("unknown", None)):
        probe = MagicMock(return_value=(status, final))
        text = f"[Page]({D}unlisted-page)"
        assert repair_twingate_links(text, LIVE, {}, probe=probe).text == text


def test_without_a_probe_unknown_links_are_kept():
    text = f"[Page]({D}not-in-sitemap)"
    assert repair_twingate_links(text, LIVE, {}).text == text


def test_probe_cache_checks_each_url_once():
    probe = MagicMock(return_value=("dead", None))
    cache: dict = {}
    repair_twingate_links(f"[A]({D}gone) [B]({D}gone#x)", LIVE, {}, probe=probe, probe_cache=cache)
    repair_twingate_links(f"[C]({D}gone)", LIVE, {}, probe=probe, probe_cache=cache)
    probe.assert_called_once_with(D + "gone")


# ── repair_reference_tree ────────────────────────────────────────────────────


def _write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def test_repair_reference_tree_rewrites_body_but_never_frontmatter(tmp_path):
    ref = tmp_path / "twingate-pam" / "references" / "x.md"
    _write(ref, f"---\nsource: {D}identity-firewall\n---\n\n- [Overview]({D}identity-firewall)\n")
    counts = repair_reference_tree(
        tmp_path, _live_many(), {D + "identity-firewall": D + "privileged-access-management"}, probe=None
    )
    assert ref.read_text(encoding="utf-8") == (
        f"---\nsource: {D}identity-firewall\n---\n\n- [Overview]({D}privileged-access-management)\n"
    )
    assert counts["files_changed"] == 1
    assert counts["rewritten"] == 1


def test_repair_reference_tree_skips_manual_references(tmp_path):
    ref = tmp_path / "twingate-pam" / "references" / "manual.md"
    text = f"<!-- manual-reference: do-not-overwrite -->\n- [Gone]({D}gone)\n"
    _write(ref, text)
    repair_reference_tree(tmp_path, _live_many(), {}, probe=MagicMock(return_value=("dead", None)))
    assert ref.read_text(encoding="utf-8") == text


def test_repair_reference_tree_does_nothing_on_a_partial_sitemap(tmp_path):
    ref = tmp_path / "twingate-pam" / "references" / "x.md"
    text = f"- [Gone]({D}gone)\n"
    _write(ref, text)
    probe = MagicMock(return_value=("dead", None))
    counts = repair_reference_tree(tmp_path, LIVE, {}, probe=probe)
    assert ref.read_text(encoding="utf-8") == text
    assert counts["files_changed"] == 0
    probe.assert_not_called()


# ── http_probe ───────────────────────────────────────────────────────────────


def _resp(status: int, url: str) -> MagicMock:
    resp = MagicMock()
    resp.status_code = status
    resp.url = url
    return resp


def test_http_probe_follows_redirects_to_a_canonical_final_url():
    with patch("reference_links.requests.head", return_value=_resp(200, D + "clients/")):
        assert http_probe(D + "download") == ("live", D + "clients")


def test_http_probe_maps_404_to_dead_and_errors_to_unknown():
    with patch("reference_links.requests.head", return_value=_resp(404, D + "gone")):
        assert http_probe(D + "gone") == ("dead", None)
    with patch("reference_links.requests.head", side_effect=requests.ConnectionError("down")):
        assert http_probe(D + "x") == ("unknown", None)
    with patch("reference_links.requests.head", return_value=_resp(500, D + "x")):
        assert http_probe(D + "x") == ("unknown", None)


def test_http_probe_falls_back_to_get_when_head_is_refused():
    with (
        patch("reference_links.requests.head", return_value=_resp(405, D + "x")),
        patch("reference_links.requests.get", return_value=_resp(200, D + "x")) as mock_get,
    ):
        assert http_probe(D + "x") == ("live", D + "x")
    mock_get.assert_called_once()
