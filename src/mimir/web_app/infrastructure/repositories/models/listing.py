from django.db import models

from .base import EntityBaseModel


class ListingModel(EntityBaseModel, models.Model):

    area_square_meters = models.IntegerField()
    listing_date = models.DateField()
    listing_details = models.JSONField()
    listing_reference_number = models.CharField(max_length=255)
    listing_updated_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=255)
    property_type = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
