#!/usr/bin/env python

from setuptools import setup

setup(
    name="wagtail-openshift-quickstart",
    version="0.1.1",
    description="Wagtail CMS quickstart for deployment on OpenShift",
    author="Timo Rieber",
    author_email="dev@timorieber.de",
    url="https://github.com/timorieber",
    install_requires=[
        "wagtail==0.8.3"
    ],
)
