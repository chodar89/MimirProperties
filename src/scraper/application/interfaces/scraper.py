from abc import ABC as Abstract, abstractmethod


class ScraperInterface(Abstract):
    
    @abstractmethod
    def process(self, url: str):
        ...
