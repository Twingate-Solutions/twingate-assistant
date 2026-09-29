"""Unit tests for url_safety.safe_get (redirect re-validation + size cap)."""

from unittest.mock import MagicMock, patch

import pytest
import requests

from url_safety import (
    REQUEST_HEADERS,
    ResponseTooLargeError,
    TooManyRedirectsError,
    safe_get,
)


def _mock_response(
    *,
    status_code: int = 200,
    content: bytes = b"",
    headers: dict | None = None,
) -> MagicMock:
    """Build a mock requests.Response usable by safe_get's streaming reader."""
    mock_resp = MagicMock()
    mock_resp.status_code = status_code
    mock_resp.headers = headers or {}
    mock_resp.iter_content = MagicMock(return_value=[content] if content else [])
    mock_resp.close = MagicMock()
    return mock_resp


# ── Happy path ───────────────────────────────────────────────────────────────


@patch("url_safety.requests.get")
def test_safe_get_returns_response_on_success(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(content=b"hello world")

    response = safe_get(
        "https://www.twingate.com/docs/x", timeout=10, headers=REQUEST_HEADERS, max_bytes=1024
    )

    assert response._content == b"hello world"
    mock_get.assert_called_once()
    call_kwargs = mock_get.call_args.kwargs
    assert call_kwargs["allow_redirects"] is False
    assert call_kwargs["stream"] is True


@patch("url_safety.requests.get")
def test_safe_get_rejects_disallowed_initial_url(mock_get: MagicMock) -> None:
    with pytest.raises(ValueError, match="disallowed"):
        safe_get("https://evil.com/x", timeout=10, max_bytes=1024)
    mock_get.assert_not_called()


# ── Redirect handling ────────────────────────────────────────────────────────


@patch("url_safety.requests.get")
def test_safe_get_follows_redirect_to_allowed_host(mock_get: MagicMock) -> None:
    redirect = _mock_response(
        status_code=302, headers={"Location": "https://help.twingate.com/articles/x"}
    )
    final = _mock_response(status_code=200, content=b"final body")
    mock_get.side_effect = [redirect, final]

    response = safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1024)

    assert response._content == b"final body"
    assert mock_get.call_count == 2
    second_call_url = mock_get.call_args_list[1].args[0]
    assert second_call_url == "https://help.twingate.com/articles/x"


@patch("url_safety.requests.get")
def test_safe_get_rejects_redirect_to_disallowed_host(mock_get: MagicMock) -> None:
    redirect = _mock_response(status_code=302, headers={"Location": "https://evil.com/steal"})
    mock_get.return_value = redirect

    with pytest.raises(ValueError, match="disallowed"):
        safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1024)

    assert mock_get.call_count == 1


@patch("url_safety.requests.get")
def test_safe_get_resolves_relative_redirect_location(mock_get: MagicMock) -> None:
    redirect = _mock_response(status_code=301, headers={"Location": "/docs/moved"})
    final = _mock_response(status_code=200, content=b"moved body")
    mock_get.side_effect = [redirect, final]

    response = safe_get("https://www.twingate.com/docs/old", timeout=10, max_bytes=1024)

    assert response._content == b"moved body"
    second_call_url = mock_get.call_args_list[1].args[0]
    assert second_call_url == "https://www.twingate.com/docs/moved"


@patch("url_safety.requests.get")
def test_safe_get_strips_authorization_on_cross_host_redirect(mock_get: MagicMock) -> None:
    redirect = _mock_response(
        status_code=302, headers={"Location": "https://help.twingate.com/articles/x"}
    )
    final = _mock_response(status_code=200, content=b"body")
    mock_get.side_effect = [redirect, final]

    safe_get(
        "https://www.twingate.com/docs/x",
        timeout=10,
        headers={"Authorization": "Bearer secret-token"},
        max_bytes=1024,
    )

    second_call_headers = mock_get.call_args_list[1].kwargs["headers"]
    assert "Authorization" not in second_call_headers


@patch("url_safety.requests.get")
def test_safe_get_keeps_authorization_on_same_host_redirect(mock_get: MagicMock) -> None:
    redirect = _mock_response(
        status_code=302, headers={"Location": "https://www.twingate.com/docs/new"}
    )
    final = _mock_response(status_code=200, content=b"body")
    mock_get.side_effect = [redirect, final]

    safe_get(
        "https://www.twingate.com/docs/x",
        timeout=10,
        headers={"Authorization": "Bearer secret-token"},
        max_bytes=1024,
    )

    second_call_headers = mock_get.call_args_list[1].kwargs["headers"]
    assert second_call_headers["Authorization"] == "Bearer secret-token"


@patch("url_safety.requests.get")
def test_safe_get_too_many_redirects_raises(mock_get: MagicMock) -> None:
    redirect = _mock_response(
        status_code=302, headers={"Location": "https://www.twingate.com/docs/loop"}
    )
    mock_get.return_value = redirect

    with pytest.raises(TooManyRedirectsError):
        safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1024, max_redirects=2)

    assert mock_get.call_count == 3  # initial + 2 redirects allowed


@patch("url_safety.requests.get")
def test_safe_get_redirect_without_location_header_raises(mock_get: MagicMock) -> None:
    redirect = _mock_response(status_code=302, headers={})
    mock_get.return_value = redirect

    with pytest.raises(ValueError, match="Location"):
        safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1024)


# ── Size cap ─────────────────────────────────────────────────────────────────


@patch("url_safety.requests.get")
def test_safe_get_aborts_when_body_exceeds_max_bytes(mock_get: MagicMock) -> None:
    big_chunk = b"x" * 2000
    response = _mock_response(status_code=200)
    response.iter_content = MagicMock(return_value=[big_chunk, big_chunk])
    mock_get.return_value = response

    with pytest.raises(ResponseTooLargeError):
        safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1000)


@patch("url_safety.requests.get")
def test_safe_get_under_cap_succeeds(mock_get: MagicMock) -> None:
    mock_get.return_value = _mock_response(status_code=200, content=b"x" * 500)

    response = safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1000)

    assert response._content == b"x" * 500


# ── params forwarding (github-style pagination) ────────────────────────────


@patch("url_safety.requests.get")
def test_safe_get_forwards_params_on_first_hop_only(mock_get: MagicMock) -> None:
    redirect = _mock_response(
        status_code=302, headers={"Location": "https://api.github.com/next-page"}
    )
    final = _mock_response(status_code=200, content=b"{}")
    mock_get.side_effect = [redirect, final]

    safe_get(
        "https://api.github.com/orgs/Twingate/repos",
        timeout=10,
        max_bytes=1024,
        params={"type": "public"},
    )

    first_call_kwargs = mock_get.call_args_list[0].kwargs
    second_call_kwargs = mock_get.call_args_list[1].kwargs
    assert first_call_kwargs["params"] == {"type": "public"}
    assert second_call_kwargs["params"] is None


# ── requests.RequestException passthrough ──────────────────────────────────


@patch("url_safety.requests.get")
def test_safe_get_propagates_request_exception(mock_get: MagicMock) -> None:
    mock_get.side_effect = requests.RequestException("connection reset")

    with pytest.raises(requests.RequestException):
        safe_get("https://www.twingate.com/docs/x", timeout=10, max_bytes=1024)
