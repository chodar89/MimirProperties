from django.contrib.auth import get_user_model
from django.contrib.auth.management.commands import createsuperuser
from django.core.management import CommandError
from django.core.management.base import CommandParser


class Command(createsuperuser.Command):
    """Borrowed from this thread:
    https://stackoverflow.com/questions/6244382/how-to-automate-createsuperuser-on-django
    """

    help = "Crate a superuser, and allow password and email to be provided"

    def add_arguments(self, parser: CommandParser) -> None:
        super().add_arguments(parser)
        parser.add_argument(
            "--password",
            dest="password",
            default=None,
            help="Specifies the password for the superuser.",
        )

    def handle(self, *args: tuple, **options: dict) -> None:
        password = options.get("password")
        username = options.get("username")
        email = options.get("email")
        database = options.get("database")

        if not email:
            raise CommandError("--email is required")

        if password and not username:
            raise CommandError("--username is required if specifying --password")

        super(Command, self).handle(*args, **options)

        if password:
            user = get_user_model()._default_manager.db_manager(database).get(username=username)
            user.set_password(password)
            user.email = email
            user.save()
