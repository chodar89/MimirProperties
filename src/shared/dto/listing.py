from attrs import frozen


@frozen(kw_only=True)
class ListingSearchParametersDto:
    city: str
    distance: int
    property_type: str
    region: str
    pagination_limit: int | None = None
