# dev.py
from .base import *

DEBUG = True

SECRET_KEY = "django-insecure-*0wqm+r3r@fwf&8@#w6-x2dgazcvq^xiy=7s$+e0-#)42bomqg"

ALLOWED_HOSTS = ["localhost", "127.0.0.1"]

# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
