from django.db import models

from .base import EntityBaseModel


class PropertyModel(EntityBaseModel, models.Model):

    area_square_meters = models.IntegerField()
    built_year = models.PositiveIntegerField()
    floor = models.IntegerField(null=True)
    is_new_build = models.BooleanField(default=True)
    listing_date = models.DateField()
    listing_reference_number = models.CharField(max_length=255)
    listing_updated_date = models.DateField(null=True)
    phone_number = models.CharField(max_length=255)
    rooms = models.IntegerField()
    title = models.CharField(max_length=255)
