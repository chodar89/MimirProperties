from attrs import Factory, field, frozen

from shared.types.http import URL
from shared.value_objects import Timeout


@frozen(kw_only=True)
class HttpRequestDto:
    url: URL
    http_method: str
    headers: dict = field(default=Factory(dict))
    payload: dict = field(default=Factory(dict))
    query_parameters: dict = field(default=Factory(dict))
    timeout: int = Timeout.FIVE_SECOND_TIMEOUT


@frozen(kw_only=True)
class HttpResponseDto:
    request_dto: HttpRequestDto
    content: str = field(repr=False, default="")
    error: Exception | None = None
    json: dict = field(repr=False, default=Factory(dict))
    status_code: int | None = None

    def is_ok(self) -> bool:
        return self.status_code == 200 and self.error is None
