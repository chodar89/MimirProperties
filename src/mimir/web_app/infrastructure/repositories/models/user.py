from django.contrib.auth.models import AbstractUser

from .base import EntityBaseModel


# type issue (https://github.com/typeddjango/django-stubs/issues/471)
class UserModel(AbstractUser, EntityBaseModel):  # type: ignore
    pass
