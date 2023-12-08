# Getting Start

## 1. Setting Up `.env` Files
- Go to directory `archeolojiMain`.
- Create `.env`
```sh
SECRET_KEY = "YourSpeacialKey"
```
## 2. Setting up Docker & Migrations & Create Super User

- You must the be directory `archeolojiMain`

```sh
docker-compose build
```

- Migration from Docker

```sh
docker-compose run django-archaeology python manage.py migrate
```

- Create Super User

```sh
docker-compose run django-archaeology python manage.py createsuperuser
```

- Run the Docker

```sh
docker-compose up
```

- Now you can go to [127.0.0.1:8000](127.0.0.1:8000) to see it live. 🚀
- Admin panel [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
- You can create what u want!