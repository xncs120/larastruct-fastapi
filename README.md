# Larastruct Fastapi - Quickstart
This is fastapi template that is inspired by laravel project folder structure

## Templates included
- [x] Register user to database
- [x] Simple JWT token generation
- [x] Authentication on secured routes
- [x] Config file and env settings
- [x] Sample user api, schema, html template, css style
- [x] Test files location
- [ ] Docker

## Tech used
### Stacks
`python` `uvicorn` `fastapi` `sqlalchemy+sqlmodel` `postgres` `html`
### Packages (version when added)
`uvicorn=0.23.2` `fastapi=0.104.0` `SQLAlchemy=2.0.30` `sqlmodel=0.0.19`
`alembic=1.13.1` `psycopg2-binary=2.9.9` `passlib==1.7.4` `bcrypt=4.1.3`
`oauthlib=3.2.2` `python-jose=3.3.0` `python-multipart=0.0.9` `Jinja2=3.1.4`

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
│   └── database.py
├── helpers/ (
│   └── __init__.py
│   └── auth_helper.py
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

