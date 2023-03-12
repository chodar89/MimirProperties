from bs4 import BeautifulSoup

from listing.application.interfaces.listing_config import ListingConfig
from scraper.application.interfaces import ScraperInterface
from shared.dto import (HttpRequestDto, HttpResponseDto,
                        ListingSearchParametersDto)
from shared.http_engines import RequestsEngine
from shared.value_objects.parsers import ResponseParser

PAGE_NUMBER = int


class BeautifulSoupScraper(ScraperInterface):

    PARSER = ResponseParser.HTML5LIB

    def __init__(self) -> None:
        self._bs = BeautifulSoup
        self._next_page: PAGE_NUMBER = 1
        self._http_engine = RequestsEngine()
        self._last_page: PAGE_NUMBER = 1

    def execute(self, dto: ListingSearchParametersDto, listing_config: ListingConfig) -> None:
        self._listing_config = listing_config
        list_response = self._process_list_view(dto=dto)
        if list_response.is_ok():
            soup = self._bs(list_response.content, self.PARSER)
            listings_container = soup.find(**listing_config.listings_container_search_tags())
            paths = [i.get("href", "") for i in listings_container.findChildren("a", href=True)]
            detail_http_requests = listing_config.detail_http_request_dtos(url_paths=paths)
            for req in detail_http_requests:
                detail_response = self._process_detail(dto=req)
                if not detail_response.is_ok():
                    continue
                soup = self._bs(detail_response.content, self.PARSER)
                dirty_price = soup.find(attrs={"data-testid": "ad-price-container"}).find("h3").text
                split_price = [s for s in dirty_price.split() if s.isdigit()]
                int("".join(split_price))

    def _process_list_view(self, dto: ListingSearchParametersDto) -> HttpResponseDto:
        http_request_dto = self._listing_config.list_http_request_dto(
            dto=dto, next_page=self._next_page
        )
        return self._http_engine.process_request(dto=http_request_dto)

    def _process_detail(self, dto: HttpRequestDto) -> HttpResponseDto:
        return self._http_engine.process_request(dto=dto)
