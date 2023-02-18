from abc import ABC as Abstract
from abc import abstractmethod

from shared.dto import HttpQueryParameters, HttpResponseDto
from shared.types.http import URL


class ListingConfig(Abstract):
    @abstractmethod
    @classmethod
    def get_base_url(cls) -> URL:
        ...

    @abstractmethod
    @classmethod
    def next_list_url(cls, query_params: HttpQueryParameters, next_page: int) -> URL:
        ...

    @abstractmethod
    @classmethod
    def detail_url(cls, dto: HttpResponseDto) -> URL:
        ...
