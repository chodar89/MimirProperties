from typing import Final

from listing.application.interfaces.listing_config import ListingConfig
from shared.dto import (HttpRequestDto, HttpResponseDto,
                        ListingSearchParametersDto)
from shared.types.http import URL


class OTODomConfig(ListingConfig):

    BASE_URL: Final[URL] = URL("https://www.otodom.pl")

    @classmethod
    def get_base_url(cls) -> URL:
        return cls.BASE_URL

    @classmethod
    def list_http_request_dto(
        cls, dto: ListingSearchParametersDto, next_page: int
    ) -> HttpRequestDto:
        url = URL(
            f"{cls.BASE_URL}/pl/wyszukiwanie/sprzedaz/{dto.property_type}/"
            f"{dto.region}/{dto.city}/{dto.city}/{dto.city}"
        )
        query_parameters = cls.parse_query_parameters(dto=dto, next_page=next_page)
        return HttpRequestDto(url=url, http_method="GET", query_parameters=query_parameters)

    @classmethod
    def detail_http_request_dtos(cls, dto: HttpResponseDto) -> list[HttpRequestDto]:
        raise NotImplementedError

    @classmethod
    def parse_query_parameters(cls, dto: ListingSearchParametersDto, next_page: int) -> dict:
        query_parameters = {
            "distanceRadius": dto.distance,
            "page": next_page,
        }
        return query_parameters
