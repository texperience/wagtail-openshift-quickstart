"""
Template for environment specific settings in wagtail-openshift-quickstart project

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

For information howto deploy django applications to production environments, see
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

"""

# Necessary imports
import os

# Admins for error reporting
ADMINS = ()

# Build paths inside this file like this: os.path.join(DATA_DIR, ...)
DATA_DIR = os.path.join(os.environ.get("OPENSHIFT_DATA_DIR", os.environ.get("HOME", "")), "wagtail-openshift-quickstart-local")

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(DATA_DIR, "media/")

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("OPENSHIFT_SECRET_TOKEN")

# SECURITY WARNING: don't run with debug turned on in production!
# Uncomment/change on development environment
#DEBUG = True
#for template_engine in TEMPLATES:
#    template_engine['OPTIONS']['debug'] = True

# Comment/delete on development environment
DEBUG = False

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
# With DEBUG = True no allowed hosts are necessary
ALLOWED_HOSTS = [
    os.environ.get("OPENSHIFT_APP_DNS"),
]

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
# You may use sqlite on your local machine
# Uncomment/change on development environment
#DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": "/path/to/mydatabase",
#    }
#}
# This quickstart uses PostgreSQL on OpenShift
# Comment/delete on development environment
DATABASES = {
    "default": {
      "ENGINE": "django.db.backends.postgresql_psycopg2",
      "NAME": os.environ.get("PGDATABASE"),
      "USER": os.environ.get("OPENSHIFT_POSTGRESQL_DB_USERNAME"),
      "PASSWORD": os.environ.get("OPENSHIFT_POSTGRESQL_DB_PASSWORD"),
    }
}

# Wagtail configurations
WAGTAIL_SITE_NAME = os.environ.get("OPENSHIFT_APP_NAME", "")
