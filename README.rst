wagtail-openshift-quickstart
============================

.. image:: https://img.shields.io/badge/version-v1.2.0-blue.svg

.. image:: https://img.shields.io/badge/license-ISC%20License%20(ISCL)-blue.svg
    :target: http://en.wikipedia.org/wiki/ISC_license

`Wagtail CMS`_ quickstart for deployment on OpenShift Online

.. _Wagtail CMS: http://wagtail.io

Prerequisites
-------------
* You have an `OpenShift account`_
* You have installed the `rhc` command line tools for `remote OpenShift administration`_

.. _OpenShift account: https://www.openshift.com
.. _remote OpenShift administration: https://developers.openshift.com/en/getting-started-client-tools.html

Recommendations
---------------
* You use `virtualenv`_ for isolated local python development
* You are familiar with `Django`_ basics, at least visited their great `online tutorial`_

.. _virtualenv: http://virtualenv.readthedocs.org/en/latest/virtualenv.html
.. _Django: https://www.djangoproject.com
.. _online tutorial: https://docs.djangoproject.com/en/dev/intro/tutorial01

Getting started
---------------

Initialize OpenShift application and local codebase
***************************************************
* Open a terminal and change into your workspace where your code will live
* Create your `Python-based`_ and `PostgreSQL-backed`_ OpenShift `application`_ with a single command

  ``rhc app create yourwagtaildemoapp python-2.7 postgresql-9.2 --from-code https://github.com/timorieber/wagtail-openshift-quickstart``

.. _Python-based: https://www.python.org
.. _PostgreSQL-backed: http://www.postgresql.org
.. _application: https://developers.openshift.com/en/getting-started-creating-applications.html

**Great!** Your application is deployed and the git repository is cloned locally into ``yourwagtaildemoapp``

Prepare OpenShift environment
*****************************
* Open a terminal session on your application server

  ``rhc ssh -a yourwagtaildemoapp``
* Change directory to your application root

  ``cd $OPENSHIFT_REPO_DIR/wsgi/wagtail-openshift-quickstart``
* Create a superuser account

  ``python manage.py createsuperuser``
* Close terminal session

  ``exit``
* Enjoy your remote production site at

  ``http://yourwagtaildemoapp-yourdomain.rhcloud.com`` (Homepage)

  ``http://yourwagtaildemoapp-yourdomain.rhcloud.com/wagtail`` (Wagtail CMS administration)

  ``http://yourwagtaildemoapp-yourdomain.rhcloud.com/django`` (Django administration)

**Congratulations!** Now you can manage and publicly view content in your production site!

Initialize local development environment
****************************************
* Prepare your system as documented in the Wagtail docs under `Getting started`_, stop before ``pip install wagtail``
* Change directory to your local repository root

  ``cd yourwagtaildemoapp``
* Install necessary python packages (includes all relevant dependencies)

  ``pip install -e .``
* Create and configure a ``local_settings.py`` (copy template from ``data/local_settings.py``) located at ``$HOME/wagtail-openshift-quickstart-local/conf``
* Change directory to your application root

  ``cd wsgi/wagtail-openshift-quickstart``
* Initialize the database structure and data

  ``python manage.py migrate``
* Create a superuser account

  ``python manage.py createsuperuser``
* Run development server

  ``python manage.py runserver``
* Enjoy your local development site at

  ``http://localhost:8000`` (Homepage)

  ``http://localhost:8000/wagtail`` (Wagtail CMS administration)

  ``http://localhost:8000/django`` (Django administration)

**Let's code!** You're ready to develop your Wagtail powered webpages.

.. _Getting started: http://docs.wagtail.io/en/stable/getting_started/index.html

**That's it! Easy, right?** You've set up an OpenShift hosted Wagtail CMS and your local development environment in 10 Minutes! Awesome!
