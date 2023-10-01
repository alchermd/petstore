# petstore

`petstore` is a webapp for managing a pet store's inventory. It has a public storefront and an administrative management backend. It is a monolithic Django application that utilizes Django Templates for the frontend, and PostgreSQL as its data store.

## Getting Started

### Prepare the database

```console
$ createdb petstore # Take note of your credentials for further usage.
```

### Install the dependencies

```console
$ python3 -m venv venv
$ source ./venv/bin/activate
$ pip install -r requirements.txt
$ cp .env.example .env # Fill out the necessary details.
```

### Run the server

```console
$ ./manage.py runserver
```
