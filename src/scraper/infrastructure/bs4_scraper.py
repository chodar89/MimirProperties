from bs4 import BeautifulSoup

from listing.application.interface.listing_config import ListingConfig
from scraper.application.interfaces import ScraperInterface
from shared.dto import HttpRequestDto
from shared.http_engines import HttpEngine
from shared.value_objects.parsers import ResponseParser


class BeautifulSoupScraper(ScraperInterface):

    PARSER = ResponseParser.HTML

    def __init__(self) -> None:
        self._bs = BeautifulSoup

    def process(
        self, dto: HttpRequestDto, listing_service_config: ListingConfig, http_engine: HttpEngine
    ) -> None:
        response = http_engine.process_request(dto=dto)
        pass
