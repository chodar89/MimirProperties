from django.db import models

from .base import EntityBaseModel
from .listing import ListingModel


class PlotModel(EntityBaseModel, models.Model):
    class Meta:
        ordering = ("-created_at",)

    currency = models.CharField(max_length=20)
    total_price = models.PositiveIntegerField()
    listing = models.ForeignKey(
        ListingModel,
        on_delete=models.CASCADE,
        related_name="price_history",
        verbose_name="Price History",
    )
