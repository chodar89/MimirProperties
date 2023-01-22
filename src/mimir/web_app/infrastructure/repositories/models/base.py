import uuid

from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, editable=False, verbose_name="Created at")
    updated_at = models.DateTimeField(
        auto_now=True, null=True, editable=False, verbose_name="Updated at"
    )

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class EntityBaseModel(TimeStampedModel, UUIDModel):
    class Meta:
        abstract = True
