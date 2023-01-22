from django.db import models

from .base import EntityBaseModel


class PropertyModel(EntityBaseModel, models.Model):

    title = models.CharField(max_length=255)
    area_square_meters = models.IntegerField()
    rooms = models.IntegerField()
    floor = models.IntegerField(null=True)
    is_new_build = models.BooleanField(default=True)
    built_year = models.PositiveIntegerField()
    listing_date = models.DateField()
    listing_updated_date = models.DateField(null=True)
    listing_reference_number = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
