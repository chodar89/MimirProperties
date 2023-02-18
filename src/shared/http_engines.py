import logging
from abc import ABC as abstract
from abc import abstractmethod
from concurrent.futures import ThreadPoolExecutor

import requests

from shared.dto import HttpRequestDto, HttpResponseDto

logger = logging.getLogger(__name__)


class HttpEngine(abstract):
    @abstractmethod
    def process_request(self, dto: HttpRequestDto) -> HttpResponseDto:
        ...

    @abstractmethod
    def process_async_requests(self, dto_list: list[HttpRequestDto]) -> list[HttpResponseDto]:
        ...


class RequestsEngine(HttpEngine):
    def process_request(self, dto: HttpRequestDto) -> HttpResponseDto:
        try:
            resp = self._request(dto)
            try:
                resp_json = resp.json()
            except requests.exceptions.JSONDecodeError:
                resp_json = {}
            return HttpResponseDto(
                request_dto=dto, status_code=resp.status_code, json=resp_json, body_text=resp.text
            )
        except Exception as e:
            logger.info("Exception raised during request. Error: %s", e)
            return HttpResponseDto(request_dto=dto, error=e)

    def process_async_requests(self, dto_list: list[HttpRequestDto]) -> list[HttpResponseDto]:
        with ThreadPoolExecutor() as executor:
            results = executor.map(self.process_request, dto_list)
        return list(results)

    def _request(self, dto: HttpRequestDto) -> requests.Response:
        req_method = getattr(requests, dto.http_method.lower())
        resp: requests.Response = req_method(
            dto.url,
            params=dto.query_parameters,
            headers=dto.headers,
            data=dto.payload,
            timeout=dto.timeout,
        )
        return resp
