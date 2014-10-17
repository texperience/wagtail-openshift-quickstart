wagtail-openshift-quickstart
============================

[Wagtail CMS](http://wagtail.io) quickstart for deployment on OpenShift

## Prerequisites
* You have an [OpenShift account](https://www.openshift.com)
* You have installed the `rhc` command line tools for [remote OpenShift administration](https://developers.openshift.com/en/getting-started-client-tools.html)

## Recommendations
* You use [virtualenv](http://virtualenv.readthedocs.org/en/latest/virtualenv.html) for isolated local python development
* You are familiar with [Django](https://www.djangoproject.com) basics, at least visited their great [online tutorial](https://docs.djangoproject.com/en/dev/intro/tutorial01)

## Getting started

### Initialize codebase
* Open a terminal and `cd` into your workspace where your code will live
* Create your [Python-based](https://www.python.org) and [PostgreSQL-backed](http://www.postgresql.org) OpenShift [application](https://developers.openshift.com/en/getting-started-creating-applications.html)  
`rhc app create yourwagtaildemoapp python-3.3 postgresql-9.2`
* `cd` into your new project  
`cd yourwagtaildemoapp`
* Remove unnecessary files and commit  
`git rm . -r`
`git commit -m "Project cleanup"`
* Add this upstream repo and pull  
`git remote add upstream -m master https://github.com/timorieber/wagtail-openshift-quickstart.git`
`git pull -s recursive -X theirs upstream master`

### Initialize local development environment
* Install necessary python packages (includes all relevant dependencies)  
`pip install wagtail`
* Create and configure a `local_settings.py` (see template below) located at `$HOME/wagtail-openshift-quickstart-local/conf`
* `cd` into the application root folder  
`cd wsgi/wagtail-openshift-quickstart`
* Initialize the database structure and data  
`python manage.py migrate`
* Create a superuser account  
`python manage.py createsuperuser`
* Run development server  
`python manage.py runserver`
* Enjoy your site at
 * `http://localhost:8000` (Homepage)
 * `http://localhost:8000/wagtail` (Wagtail CMS administration)
 * `http://localhost:8000/django` (Django administration)

### Prepare OpenShift environment
* `ssh` onto your application server
`ssh userid@yourwagtaildemoapp-yourdomain.rhcloud.com`
* Create and configure a `local_settings.py` (see template below) located at `$OPENSHIFT_DATA_DIR/wagtail-openshift-quickstart-local/conf` (path does not exist by default)

### Deploy on OpenShift
* Back on your local machine push upstream to origin  
`git push origin master`
* Enjoy your site at
 * `http://yourwagtaildemoapp-yourdomain.rhcloud.com` (Homepage)
 * `http://yourwagtaildemoapp-yourdomain.rhcloud.com/wagtail` (Wagtail CMS administration)
 * `http://yourwagtaildemoapp-yourdomain.rhcloud.com/django` (Django administration)

## Template for `local_settings.py`
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
    DATA_DIR = os.path.join(os.environ.get("HOME"), "wagtail-openshift-quickstart-local")
    # Uncomment/change production environment
    #DATA_DIR = os.path.join(os.environ.get("OPENSHIFT_DATA_DIR"), "wagtail-openshift-quickstart-local")

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = "make-this-random-and-keep-secret"

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True
    TEMPLATE_DEBUG = True

    # https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
    # With DEBUG = True no allowed hosts are necessary
    ALLOWED_HOSTS = []
    # Uncomment and change on production environment
    #ALLOWED_HOSTS = [
    #    "yourwagtaildemoapp-yourdomain.rhcloud.com",
    #]

    # Database
    # https://docs.djangoproject.com/en/dev/ref/settings/#databases
    # You may use sqlite on your local machine
    # Comment/delete on production environment
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": "/path/to/mydatabase",
        }
    }
    # This quickstart uses PostgreSQL on OpenShift
    # Uncomment/change on production environment
    #DATABASES = {
    #    "default": {
    #    "ENGINE": "django.db.backends.postgresql_psycopg2",
    #    "NAME": os.environ.get("PGDATABASE"),
    #    "USER": os.environ.get("OPENSHIFT_POSTGRESQL_DB_USERNAME"),
    #    "PASSWORD": os.environ.get("OPENSHIFT_POSTGRESQL_DB_PASSWORD"),
    #    }
    #}

