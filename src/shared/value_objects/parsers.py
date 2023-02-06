from enum import StrEnum  # type: ignore


class ResponseParser(StrEnum):
    HTML = "html.parser"
    LXML = "lxml"
    LXML_XML = "xml-xml"
    HTML5LIB = "html5lib"
