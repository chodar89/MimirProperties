from abc import ABC as Abstract
from abc import abstractmethod

from shared.dto import HttpResponseDto
from shared.types.http import URL


class ListingConfig(Abstract):
    @abstractmethod
    def next_list_url(self, query_params: dict) -> None:
        ...

    @abstractmethod
    def detail_url(self, dto: HttpResponseDto) -> URL:
        ...
