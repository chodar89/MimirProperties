from django.db import models

from .base import EntityBaseModel


class PlotModel(EntityBaseModel, models.Model):

    area_square_meters = models.IntegerField()
    is_private = models.BooleanField()
    listing_date = models.DateField()
    listing_reference_number = models.CharField(max_length=255)
    listing_updated_date = models.DateField(null=True)
    media = models.JSONField()
    phone_number = models.CharField(max_length=255)
    plot_id = models.CharField(max_length=255)
    plot_type = models.CharField(max_length=255)
    road_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
