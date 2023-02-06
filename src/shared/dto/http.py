from dataclasses import dataclass, field


@dataclass
class HttpRequestDto:

    URL: str
    http_method: str
    headers: dict = field(default_factory=dict)
    payload: dict = field(default_factory=dict)
    query_parameters: dict = field(default_factory=dict)
    timeout: int = 5


@dataclass
class HttpResponseDto:
    request_dto: HttpRequestDto
    body_text: str = ""
    error: Exception | None = None
    json: dict = field(default_factory=dict)
