from django.urls import path

from .scraper.views import ScrapeDataView

urlpatterns = [
    path("scrape-data", ScrapeDataView.as_view(), name="scrape-data"),
]
