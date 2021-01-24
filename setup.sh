#!/bin/bash

virtualenv project_name

py -m venv name_env

py -m pip install --upgrade pip

# <DIR>\Scripts\activate
source time_env/Scripts/activate

py -m pip install django

# django-admin startproject name_project

py manage.py makemigrations

py manage.py migrate

py manage.py runserver

py manage.py startapp core apps/core

py manage.py startapp apps/userprofile

py manage.py startapp team apps/team

