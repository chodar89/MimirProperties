from django.contrib.auth.models import AbstractUser

from .base import EntityBaseModel


class UserModel(AbstractUser, EntityBaseModel):  # type: ignore https://github.com/typeddjango/django-stubs/issues/471
    pass
