from django.urls import path

from .scraper.views import ListingServicesView, ScrapeDataView

urlpatterns = [
    path("listing-services", ListingServicesView.as_view(), name="listing_services"),
    path("scrape-data", ScrapeDataView.as_view(), name="scrape_data"),
]
