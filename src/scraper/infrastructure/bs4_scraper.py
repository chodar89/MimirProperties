from bs4 import BeautifulSoup

from scraper.application.interfaces import ScraperInterface
from shared.dto import HttpRequestDto
from shared.http_engines import HttpEngine
from shared.value_objects.parsers import ResponseParser


class BeautifulSoupScraper(ScraperInterface):

    PARSER = ResponseParser.HTML

    def __init__(self) -> None:
        self._bs = BeautifulSoup

    def process(self, dto: HttpRequestDto, http_engine: HttpEngine) -> None:
        ...
