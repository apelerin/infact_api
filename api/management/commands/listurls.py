from typing import Any

from django.core.management import BaseCommand

from django.core.management import call_command
from django_extensions.management.commands.show_urls import (
    Command as ExtensionCommand,
)


class Command(BaseCommand):
    help = (
        "List all available URLS, associated Python function and reverse names"
    )

    def handle(self, *args: Any, **options: Any) -> None:
        call_command(ExtensionCommand())
