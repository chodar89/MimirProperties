from django.urls import path

from .scraper.views import ListingServicesView

urlpatterns = [
    path("listing-services", ListingServicesView.as_view(), name="listing_services"),
]
