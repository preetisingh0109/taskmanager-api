# Task Manager API

A REST API built with **Python, Django and Django REST Framework**: JWT authentication, per-user task CRUD, filtering, search, ordering, pagination, Swagger docs and automated tests.

## Features
- JWT auth (register, login, refresh) via `djangorestframework-simplejwt`
- Task CRUD with ownership enforcement (users only see their own tasks)
- Filter by `status`, `priority`, `due_date`; search by title/description; ordering
- Custom action: `POST /api/tasks/{id}/complete/`
- Interactive API docs (OpenAPI/Swagger) at `/api/docs/`
- Unit tests with `APITestCase`

## Setup
```bash
git clone <your-repo-url> && cd taskmanager-api
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser   # optional
python manage.py runserver
```
Docs: http://127.0.0.1:8000/api/docs/

## Endpoints
| Method | URL | Description |
|---|---|---|
| POST | `/api/auth/register/` | Create account |
| POST | `/api/auth/login/` | Get access + refresh token |
| POST | `/api/auth/refresh/` | Refresh access token |
| GET/POST | `/api/tasks/` | List (paginated) / create |
| GET/PUT/PATCH/DELETE | `/api/tasks/{id}/` | Retrieve / update / delete |
| POST | `/api/tasks/{id}/complete/` | Mark as done |

Query examples: `/api/tasks/?status=todo&priority=3&search=report&ordering=-due_date`

## Example
```bash
curl -X POST localhost:8000/api/auth/register/ -H "Content-Type: application/json" \
  -d '{"username":"preeti","password":"strongpass1"}'
curl -X POST localhost:8000/api/auth/login/ -H "Content-Type: application/json" \
  -d '{"username":"preeti","password":"strongpass1"}'
curl localhost:8000/api/tasks/ -H "Authorization: Bearer <access_token>"
```

## Tests
```bash
python manage.py test
```

## Tech
Python 3.11+, Django 5, DRF, SimpleJWT, django-filter, drf-spectacular, SQLite (swap to PostgreSQL via `DATABASES`).
