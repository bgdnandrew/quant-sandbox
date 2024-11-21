#!/usr/bin/env python
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    # Check for --settings flag
    if "--settings" not in sys.argv:
        # Check for environment variable
        if not os.getenv("DJANGO_SETTINGS_MODULE"):
            # Default to development settings
            os.environ.setdefault(
                "DJANGO_SETTINGS_MODULE", "quant_sandbox.settings.dev"
            )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django.") from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
