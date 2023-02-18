import logging
from typing import Any

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

log = logging.getLogger(__name__)


class URL(str):
    def __new__(cls, string: Any) -> "URL":
        url = super().__new__(cls, string)
        url_validator = URLValidator(verify_exists=False)
        try:
            url_validator(url)
        except ValidationError as e:
            log.info("Invalid URL. Error: %s", e)
            raise ValueError("Invalid URL")
        return url
