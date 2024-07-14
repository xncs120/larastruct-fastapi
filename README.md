# Larastruct Fastapi - Quickstart
This is fastapi template that is inspired by laravel project folder structure.\
**Note: This implementation serves as guidance or reference and is not intended as a complete, production-ready solution.

## Templates included
- [x] Database connection (Postgres)
- [ ] Alembic migration
- [x] Register user
- [x] Simple JWT token generation
- [x] Authentication on secured routes
- [x] Config file and env settings
- [x] Orm wrapper (Warpping SQLAlchemy + SQLModel `only include most used query`)
- [x] Sample user api, schema, html, css
- [x] Test files location
- [x] Docker localhost

## Tech used
### Stacks
`python` `uvicorn` `fastapi` `sqlalchemy+sqlmodel` `postgres` `html`
### Packages (version when added)
`uvicorn=0.23.2` `fastapi=0.104.0` `SQLAlchemy=2.0.30` `sqlmodel=0.0.19`
`alembic=1.13.1` `psycopg2-binary=2.9.9` `passlib==1.7.4` `bcrypt=4.1.3`
`oauthlib=3.2.2` `python-jose=3.3.0` `python-multipart=0.0.9` `Jinja2=3.1.4`

## Installation
Download and install python\
Download and install [docker](https://www.docker.com/products/docker-desktop/)
```sh
git clone https://github.com/THIS-REPO.git
cd THIS-REPO
docker-compose up
```

## Folder structure
```sh
app/
├── controllers/
│   └── __init__.py
│   └── auth_controller.py
│   └── user_controller.py
├── core/
│   └── __init__.py
│   └── config.py
│   └── orm.py
├── middlewares/
│   └── __init__.py
│   └── oauth_middleware.py
├── migrations/
│   └── versions/
│       └── (auto-generated migration files)
├── models/
│   └── __init__.py
│   └── user_model.py
├── routes/
│   └── __init__.py
│   └── apis.py
│   └── webs.py
├── schemas/
│   └── __init__.py
│   └── auth_schema.py
│   └── user_schema.py
├── services/
│   └── __init__.py
│   └── auth_services.py
├── statics/
│   └── style.css
├── templates/
│   └── index.html
├── tests/
│   └── __init__.py
│   └── test_user.py
├── __init__.py
├── .env
├── alembic.ini
├── Dockerfile
├── main.py
├── requirements.txt
```

## Reference and external source
- [Fastapi](https://fastapi.tiangolo.com/)
- [Laravel](https://laravel.com/)
