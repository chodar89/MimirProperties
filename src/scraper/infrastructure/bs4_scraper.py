from bs4 import BeautifulSoup
from scraper.application.interfaces import ScraperInterface


class BeautifulSoupScraper(ScraperInterface):
    
    HTML_PARSER = 'html.parser'
    
    def __init__(self):
        self._bs = BeautifulSoup
    ...
    
    def process(self, url: str):
        
    
    def _make_request(self)
