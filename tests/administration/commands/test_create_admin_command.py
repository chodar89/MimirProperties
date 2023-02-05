import pytest
from django.contrib.auth import get_user_model
from django.core.management import call_command


@pytest.mark.django_db
def test_should_command_create_admin_user():
    args = ("--noinput",)
    options = {"password": "admin", "username": "admin", "email": "admin@test.com"}
    call_command("create_admin", *args, **options)
    admin_user = get_user_model().objects.filter(username="admin").first()
    assert admin_user
    assert admin_user.is_superuser is True
    assert admin_user.username == options["username"]
    assert admin_user.email == options["email"]
