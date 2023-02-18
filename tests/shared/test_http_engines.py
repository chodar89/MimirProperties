from unittest.mock import MagicMock

from shared.dto import HttpRequestDto
from shared.http_engines import RequestsEngine


def test_should_call_request_with_correct_arguments(monkeypatch):
    requests_mock = MagicMock()
    monkeypatch.setattr("shared.http_engines.requests", requests_mock)
    dto = HttpRequestDto(
        url="https://krusty-krab-burgers.com/menu",
        http_method="GET",
        headers={"Content-Type": "application/json"},
        query_parameters={"vegan": False},
        timeout=2,
    )

    resp = RequestsEngine().process_request(dto)

    requests_mock.get.assert_called_once_with(
        "https://krusty-krab-burgers.com/menu",
        params={"vegan": False},
        headers={"Content-Type": "application/json"},
        data={},
        timeout=2,
    )
    requests_mock.get().json.assert_called_once()
    assert resp.request_dto == dto
    assert resp.json == requests_mock.get().json()
    assert resp.body_text == requests_mock.get().text


def test_should_call_request_multiple_times(monkeypatch):
    request_mock = MagicMock()
    monkeypatch.setattr(RequestsEngine, "_request", request_mock)
    dto_one = HttpRequestDto(
        url="https://krusty-krab-burgers.com/menu",
        http_method="GET",
        headers={"Content-Type": "application/json"},
        query_parameters={"vegan": False},
        timeout=2,
    )

    dto_two = HttpRequestDto(
        url="https://krusty-krab-burgers.com/delivery",
        http_method="GET",
        headers={"Content-Type": "application/json"},
        query_parameters={"vegan": True},
        timeout=2,
    )

    responses = RequestsEngine().process_async_requests([dto_one, dto_two])

    assert len(responses) == 2
    assert request_mock.call_count == 2


def test_should_handle_request_errors_gracefully(monkeypatch):
    class HttpError(Exception):
        pass

    def mock_request(*args):
        raise HttpError

    monkeypatch.setattr("shared.http_engines.RequestsEngine._request", mock_request)

    dto = HttpRequestDto(
        url="https://krusty-krab-burgers.com/menu",
        http_method="GET",
        headers={"Content-Type": "application/json"},
        query_parameters={"vegan": False},
        timeout=2,
    )

    resp = RequestsEngine().process_request(dto)

    assert type(resp.error) == HttpError
    assert resp.json == {}
    assert resp.body_text == ""
