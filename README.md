# Train Station Service

REST API for a railway station: stations, routes, trains, trips, crew, and ticket orders. Users authenticate with JWT.
Email is the username.

## Stack

- Python 3.14, Django 6, Django REST Framework
- SimpleJWT, django-filter
- PostgreSQL 18
- Docker Compose
- Swagger / ReDoc and Django Debug Toolbar when `APP_ENV=development`

## Database Schema

The following diagram illustrates the database structure and relationships between models.
<img width="1107" height="885" alt="Screenshot 2026-10-29 122725" src="https://github.com/user-attachments/assets/74016e46-d06e-469b-996c-2509a72445b5" />


## Quick start (Docker)

1. Copy env and fill in values:

   ```bash
   cp .env.example .env
   ```

2. For Compose, typical database settings:

   ```env
   POSTGRES_USER=station
   POSTGRES_PASSWORD=station
   POSTGRES_DB=station
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   APP_ENV=development
   SECRET_KEY=change-me
   JWT_SECRET=change-me-too
   ```

   `POSTGRES_HOST` must be `db` (the Compose service name) when the API runs in Docker.

3. Start the stack:

   ```bash
   docker compose up --build
   ```

4. API: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
   Adminer (DB UI): [http://127.0.0.1:8080](http://127.0.0.1:8080)

Create a staff user (needed to write catalog data):

```bash
docker compose exec api python manage.py createsuperuser
```

## Local run (without Docker for the API)

Install [Pipenv](https://pipenv.pypa.io/), then:

```bash
pipenv install --dev
pipenv shell
python manage.py migrate
python manage.py runserver
```

Postgres must be reachable with the same variables as in `.env`.

## Environment

| Variable     | Purpose                                                                                |
|--------------|----------------------------------------------------------------------------------------|
| `POSTGRES_*` | Database name, user, password, host, port                                              |
| `APP_ENV`    | `development` or `production`. Development enables `DEBUG`, Swagger, and Debug Toolbar |
| `SECRET_KEY` | Django secret                                                                          |
| `JWT_SECRET` | HMAC key used to sign and verify access/refresh tokens                                 |

Do not commit `.env`.

## Auth

1. `POST /api/users/register/` — `email`, `password` (required, min 8 chars, Django password validators), optional
   `first_name`, `last_name`
2. `POST /api/users/login/` — `email`, `password` → `access` + `refresh`
3. `POST /api/users/token-refresh/` — `refresh` → new `access`
4. `GET` / `PUT` / `PATCH /api/users/me/` — current user. Password is optional on update

Send the access token as:

```http
Authorization: Bearer <access>
```

Access tokens last 5 minutes; refresh tokens last 7 days.

## Permissions

- Catalog (`stations`, `routes`, `trains`, `train-types`, `trips`, `crews`): authenticated users can read; staff can
  create/update (trips also support delete)
- Orders: any authenticated user can create/list/retrieve **their own** orders only
- Anonymous users cannot browse the catalog

## Railway API

Base path: `/api/railway/`

| Resource    | List / create   | Detail                                                                                                                    |
|-------------|-----------------|---------------------------------------------------------------------------------------------------------------------------|
| Stations    | `/stations/`    | no retrieve; search by `name`                                                                                             |
| Train types | `/train-types/` | no retrieve                                                                                                               |
| Trains      | `/trains/`      | `/trains/{id}/` — filter `train_type`, search `name`                                                                      |
| Routes      | `/routes/`      | `/routes/{id}/`                                                                                                           |
| Trips       | `/trips/`       | `/trips/{id}/` — filter `route__source_id`, `route__destination_id`; list includes `sold_tickets` and `tickets_available` |
| Crews       | `/crews/`       | `/crews/{id}/` — search `first_name`, `last_name`                                                                         |
| Orders      | `/orders/`      | `/orders/{id}/`                                                                                                           |

Create an order with at least one ticket:

```json
{
  "tickets": [
    {
      "trip": 1,
      "car": 1,
      "seat": 12
    }
  ]
}
```

Car and seat must fit the train. The same car/seat on the same trip cannot be sold twice.

## Docs (development only)

- Swagger: [http://127.0.0.1:8000/api/doc/swagger/](http://127.0.0.1:8000/api/doc/swagger/)
- ReDoc: [http://127.0.0.1:8000/api/doc/redoc/](http://127.0.0.1:8000/api/doc/redoc/)
- OpenAPI schema: [http://127.0.0.1:8000/api/schema/](http://127.0.0.1:8000/api/schema/)
- Django admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Lint

```bash
ruff check .
flake8
```
