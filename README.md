# petstore

`petstore` is a webapp for managing a pet store's inventory. It has a public storefront and an administrative management backend. It is a monolithic Django application that utilizes Django Templates for the frontend, and PostgreSQL as its data store.

## Getting Started

PetStore uses Docker and Docker Compose for local development.

```console
$ cp .env.example .env # Customized as necessary
$ docker compose up --build # Will block the current terminal, open a new one for the admin commands
```
You can now access the site at http://localhost:8000/

```console
$ ./run django migrate
$ ./run django createsuperuser
```

At this point, you can now log into the admin panel at http://localhost:8000/login
