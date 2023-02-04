import requests
from bs4 import BeautifulSoup
from requests import Response

from scraper.application.interfaces import ScraperInterface


class BeautifulSoupScraper(ScraperInterface):

    HTML_PARSER = "html.parser"
    OTODOM = "https://www.otodom.pl/pl/wyszukiwanie/sprzedaz/dzialka/warminsko--mazurskie/olsztyn/olsztyn/olsztyn?distanceRadius=5&page=1&limit=36&market=ALL&ownerTypeSingleSelect=ALL&by=DEFAULT&direction=DESC&viewType=listing"

    def __init__(self) -> None:
        self._bs = BeautifulSoup

    def process(self, url: str) -> None:
        response = self._make_request(url)
        self._bs(response.text, self.HTML_PARSER)

    def _make_request(self, url: str) -> Response:
        return requests.get(self.OTODOM)
