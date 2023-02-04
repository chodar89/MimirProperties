from abc import ABC as Abstract
from abc import abstractmethod


class ScraperInterface(Abstract):
    @abstractmethod
    def process(self, url: str) -> None:
        ...
