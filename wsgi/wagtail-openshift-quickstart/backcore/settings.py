"""
Global settings in wagtail-openshift-quickstart project

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

For information howto deploy django applications to production environments, see
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

"""

# Necessary imports
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(__file__), "../../..")

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT =  os.path.join(BASE_DIR, "wsgi/static")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/dev/howto/static-files/
STATIC_URL = "/static/"

# Additional locations of static files
STATICFILES_DIRS = (
)

STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    "compressor.finders.CompressorFinder",
)

# Application definition
INSTALLED_APPS = (
    # Default django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Third party apps
    "compressor",
    "taggit",
    "modelcluster",

    "wagtail.wagtailcore",
    "wagtail.wagtailadmin",
    "wagtail.wagtaildocs",
    "wagtail.wagtailsnippets",
    "wagtail.wagtailusers",
    "wagtail.wagtailimages",
    "wagtail.wagtailembeds",
    "wagtail.wagtailsearch",
    "wagtail.wagtailredirects",
    "wagtail.wagtailforms",

    # Own apps
    "frontcore",
)

# List of callables that know how to import templates from various sources
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.wagtailcore.middleware.SiteMiddleware",
    "wagtail.wagtailredirects.middleware.RedirectMiddleware",
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.core.context_processors.request",
)

ROOT_URLCONF = "backcore.urls"

SITE_ID = 1

# Authentication
# https://docs.djangoproject.com/en/dev/topics/auth/
LOGIN_URL = "wagtailadmin_login"

LOGIN_REDIRECT_URL = "wagtailadmin_home"

# Wagtail configurations
WAGTAIL_SITE_NAME = "wagtail-openshift-quickstart"

# django-compressor settings
COMPRESS_PRECOMPILERS = (
    ("text/x-scss", "django_libsass.SassCompiler"),
)

# Internationalization
# https://docs.djangoproject.com/en/dev/topics/i18n/
LANGUAGES = (
    ("en", "English"),
)

LANGUAGE_CODE = "en"

USE_I18N = True

USE_L10N = True

# Timezone awareness
# https://docs.djangoproject.com/en/dev/topics/i18n/timezones/
import warnings
warnings.filterwarnings("error", r"DateTimeField .* received a naive datetime", RuntimeWarning, r"django\.db\.models\.fields")
USE_TZ = True

TIME_ZONE = "Europe/London"

# Import environment specific settings
with open(os.path.join(os.environ.get("OPENSHIFT_DATA_DIR", os.environ.get("HOME")), "wagtail-openshift-quickstart-local/conf", "local_settings.py")) as f:
    exec(f.read(), globals())

