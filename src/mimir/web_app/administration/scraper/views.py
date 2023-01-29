from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from shared.value_objects.listing_service.listings import ListingServiceName


class ScrapeDataView(LoginRequiredMixin, TemplateView):

    template_name = "admin/scrape_data.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        context = super().get_context_data(**kwargs)
        context["listing_services"] = [i for i in ListingServiceName]
        return context
