
# BLOG REST API

A Simple Blog REST API for learning Django REST Framework.


## Features

- Has all CURD (Create, Update, Read, Delete) operations.
- Added token authentication using dj-rest-auth & django-allauth package
- Added authorization i.e added project-level, views level and custom permissions to api endpoints.
- Created schemas and documentations with drf-yasg package

## Run Locally

Clone the project

```bash
  git clone https://github.com/suraj-py/Blog-REST-API.git
```

Go to the project directory

```bash
  cd Blog-REST-API
```

Create virtual environment

```bash
  pipenv shell
```

If you don't have pipenv, install it using pip

```bash
  pip3 install pipenv
```

Install dependencies, this will install all require packages from Pipefile.lock

```bash
  pipenv sync
```

Start the server

```bash
  python manage.py runserver
```

Now visit http://127.0.0.1:8000/swagger/ to know and test all api endpoints.


## Screenshots

![App Screenshot](ss%20-%20Blog%20RESTAPI.png)


## Acknowledgements

 - [Django for APIs](https://djangoforapis.com/)


