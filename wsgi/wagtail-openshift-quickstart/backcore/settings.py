"""
Global settings in this project

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/

For information howto deploy django applications to production environments, see
https://docs.djangoproject.com/en/dev/howto/deployment/checklist/

"""

# Necessary imports
import os

# Build paths within the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(os.path.dirname(__file__), "../../..")

# Build paths to the persistent data directory for this project like this: os.path.join(DATA_DIR, ...)
# Set default to $HOME/project (may be symlinked) when not on OpenShift
DATA_DIR = os.environ.get("OPENSHIFT_DATA_DIR", os.path.join(os.environ.get("HOME"), "wagtail-openshift-quickstart"))

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/media/"

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
)

# Application definition
INSTALLED_APPS = (
    # Own apps
    "frontcore",

    # Wagtail apps
    "wagtail.wagtailredirects",
    "wagtail.wagtailsites",
    "wagtail.wagtailusers",
    "wagtail.wagtaildocs",
    "wagtail.wagtailimages",
    "wagtail.wagtailsearch",
    "wagtail.wagtailadmin",
    "wagtail.wagtailcore",

    # Wagtail dependencies
    "modelcluster",
    "taggit",

    # Django apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)

# Template system settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                "django.core.context_processors.request",
            ],
        },
    },
]

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

ROOT_URLCONF = "backcore.urls"

SITE_ID = 1

# Authentication
# https://docs.djangoproject.com/en/dev/topics/auth/
LOGIN_URL = "wagtailadmin_login"

LOGIN_REDIRECT_URL = "wagtailadmin_home"

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
with open(os.path.join(DATA_DIR, "conf", "local_settings.py")) as local_settings:
    exec(local_settings.read(), globals())
