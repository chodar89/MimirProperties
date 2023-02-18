from attrs import field, frozen


@frozen(kw_only=True)
class HttpRequestDto:

    url: str
    http_method: str
    headers: dict = field(default=dict)
    payload: dict = field(default=dict)
    query_parameters: dict = field(default=dict)
    timeout: int = 5


@frozen(kw_only=True)
class HttpResponseDto:
    request_dto: HttpRequestDto
    body_text: str = field(repr=False, default="")
    error: Exception | None = field(default=None)
    json: dict = field(repr=False, default=dict)
