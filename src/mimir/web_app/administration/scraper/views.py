from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, View

from shared.value_objects.listing_service.listings import ListingServiceName


class ListingServicesView(LoginRequiredMixin, TemplateView):

    template_name = "admin/listing_services.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context["listing_services"] = [i for i in ListingServiceName]
        return context


class ScrapeDataView(View):

    template_name = "admin/scrape_data.html"

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        # TODO: call ScrapeService and process. Will need to do as background task
        return redirect("listing_services")
