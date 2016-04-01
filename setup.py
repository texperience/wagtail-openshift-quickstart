#!/usr/bin/env python

from setuptools import setup

setup(
    name="wagtail-openshift-quickstart",
    version="1.3a0",
    description="Wagtail CMS quickstart for deployment on OpenShift",
    author="Timo Rieber",
    author_email="trieber@texperience.de",
    url="https://github.com/texperience",
    install_requires=[
        "django>=1.8,<1.8.99",
        "django-appconf>=1.0,<1.1",
        "psycopg2>=2.5.4",
        "wagtail>=1.4,<1.5",
    ],
)
