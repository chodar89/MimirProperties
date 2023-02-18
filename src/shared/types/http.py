from typing import Any


class URL(str):
    def __new__(cls, string: Any) -> "URL":
        url = super().__new__(cls, string)
        if not url.startswith("http://") or not url.startswith("https://"):
            raise ValueError("Invalid URL")
        return url
