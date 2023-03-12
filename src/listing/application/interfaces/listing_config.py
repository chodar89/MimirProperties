from abc import ABC as Abstract
from abc import abstractmethod

from shared.dto import (HttpRequestDto, HttpResponseDto,
                        ListingSearchParametersDto)
from shared.types.http import URL


class ListingConfig(Abstract):
    @classmethod
    @abstractmethod
    def get_base_url(cls) -> URL:
        ...

    @classmethod
    @abstractmethod
    def list_http_request_dto(
        cls, dto: ListingSearchParametersDto, next_page: int
    ) -> HttpRequestDto:
        ...

    @classmethod
    @abstractmethod
    def detail_http_request_dtos(cls, url_paths: list[str]) -> list[HttpRequestDto]:
        ...

    @classmethod
    @abstractmethod
    def listings_container_search_tags(cls) -> dict:
        ...

    @classmethod
    @abstractmethod
    def _parse_query_parameters(cls, dto: ListingSearchParametersDto, next_page: int) -> dict:
        ...
