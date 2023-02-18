from typing import Final

from listing.application.interface.listing_config import ListingConfig
from shared.dto import HttpQueryParameters, HttpResponseDto
from shared.types.http import URL


class OTODomConfig(ListingConfig):

    BASE_URL: Final[URL] = URL("https://www.otodom.pl")

    @classmethod
    def get_base_url(cls) -> URL:
        return cls.BASE_URL

    @classmethod
    def next_list_url(cls, query_params: HttpQueryParameters, next_page: int) -> URL:
        url = URL(
            f"{cls.BASE_URL}/pl/wyszukiwania/sprzedaz/{query_params.property_type}/"
            f"{query_params.region}/{query_params.city}/distanceRadius={query_params.distance}"
            f"&page={next_page}"
        )
        raise url

    @classmethod
    def detail_url(cls, dto: HttpResponseDto) -> URL:
        raise NotImplementedError
