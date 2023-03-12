from typing import Final

from listing.application.interfaces.listing_config import ListingConfig
from shared.dto import (HttpRequestDto, HttpResponseDto,
                        ListingSearchParametersDto)
from shared.types.http import URL


class OLXConfig(ListingConfig):

    BASE_URL: Final[URL] = URL("https://www.olx.pl")

    _property_type_mapping = {
        "apartment": "mieszkania",
    }

    @classmethod
    def get_base_url(cls) -> URL:
        return cls.BASE_URL

    @classmethod
    def list_http_request_dto(
        cls, dto: ListingSearchParametersDto, next_page: int
    ) -> HttpRequestDto:
        property_mapping = cls._property_type_mapping.get(dto.property_type, "")
        property_type = f"/{property_mapping}" if property_mapping else ""
        url = URL(f"{cls.BASE_URL}/nieruchomosci{property_type}/sprzedaz/" f"{dto.city}/")
        query_parameters = cls._parse_query_parameters(dto=dto, next_page=next_page)
        return HttpRequestDto(url=url, http_method="GET", query_parameters={})

    @classmethod
    def detail_http_request_dtos(cls, url_paths: list[str]) -> list[HttpRequestDto]:
        listing_urls = [URL(f"{cls.BASE_URL}/{path}") for path in url_paths if path]
        dtos = []
        for url in listing_urls:
            dto = HttpRequestDto(url=url, http_method="GET", query_parameters={})
            dtos.append(dto)
        return dtos

    @classmethod
    def listings_container_search_tags(cls) -> dict:
        return {"attrs": {"data-testid": "listing-grid"}}

    @classmethod
    def _parse_query_parameters(cls, dto: ListingSearchParametersDto, next_page: int) -> dict:
        query_parameters = {
            "distanceRadius": dto.distance,
            "page": next_page,
            "viewType": "listing",
            "limit": 3,
        }
        return query_parameters
