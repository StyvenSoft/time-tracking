# Time Tracking

Practical application project for time tracking with django and vue.
Implementation of the software as a service (saas) distribution model

## Upgrading pip


```sh
py -m pip install --upgrade pip
```

## Create a virtual environment and activate it

```sh
python -m venv env

source time_env/Scripts/activate
```

## Install Django and create an empty project

```sh
pip install django

django-admin startproject name_project
```

## Initialize database

```sh
python manage.py makemigrations
python manage.py migrate
```

## Initialize the database and create a super user

```sh
python manage.py createsuperuser

pyhton manage.py runserver
```