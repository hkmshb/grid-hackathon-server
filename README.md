# GRID Hackathon Proxy Server

Proxy server providing RESTful API for querying and retrieving datasets from GRID GeoServer and/or Data Portal.

## Installing

Create and activate a python virtual environment

```sh
$ pip install virtualenv
$ virtualenv .venv
$ . .venv/bin/activate
```

This project uses [poetry](https://poetry.eustace.io/) in place of `pip` for packaging, dependency management and installations. Thus install `poetry` then use it to install project dependencies.

```sh
(venv)$ pip install poetry
(venv)$ poetry install
```

## Running

To launch the application, create and update a `.env` file based on the `.env.tmpl` template file, then:

```sh
(venv)$ source .env
(venv)$ python manage.py run
```

for other available command line options, include the `--help` flag.

To run included unit test:

```sh
(venv)$ py.test
```
