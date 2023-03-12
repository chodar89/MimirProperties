from abc import ABC as Abstract
from abc import abstractmethod

from listing.application.interfaces.listing_config import ListingConfig
from shared.dto import (HttpRequestDto, HttpResponseDto,
                        ListingSearchParametersDto)


class ScraperInterface(Abstract):
    @abstractmethod
    def execute(self, dto: ListingSearchParametersDto, listing_config: ListingConfig) -> None:
        ...
