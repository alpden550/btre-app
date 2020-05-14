# BT Real Estate App

Django web-app to manage real estate service, realtors, listing and property inquiries.

Site example: [https://appssale.ru](https://appssale.ru)

## How to install

Download code or clone it from Github, and install dependencies.

If you have already installed Poetry, type command:

```bash
poetry install --no-dev
```

Or should use a virtual environment for the best project isolation. Activate venv and install dependencies:

```bash
pip install -r requirements.txt
```

And add environment variables:

```env
POSTGRES_HOST=postgres host
POSTGRES_DB=postgres
POSTGRES_USER=user
POSTGRES_PASSWORD=password

SECRET_KEY=secret key

EMAIL_HOST=email smtp host
EMAIL_PORT=587
EMAIL_HOST_USER=emal user
EMAIL_HOST_PASSWORD=email password
```

Run docker-compose to start redis and postgres:

```bash
docker-compose up
```

And run celery:

```bash
celery worker -A btre --loglevel=debug --concurrency=4
```

## How to run local:

```bash
python manage.py migrate
python manage.py runserver
```
