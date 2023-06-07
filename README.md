# FOODGRAM

Приложение «Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

### Технологии 
- Python
- Django
- Django REST Framework
- Postgres
- Docker
- Djoser
- Yandex Cloud
- Docker
- CI/CD

### Как развернуть проект на удаленном сервере

- Склонировать репозиторий
```commandline
git clone
```
- Для работы с проектом локально необходимо установить Docker и Docker-compose и выполнить команды для сборки контейнеров:

```commandline
cd infra
docker-compose up -d --build
```
- Для работы с проектом на сервере необходимо установить Docker и Docker-compose. 
 
- Внутри контейнера необходимо выполнить миграции и собрать статику приложения, по необходимости создать суперюзера:
```commandline
docker container exec -it <CONTAINER ID> bash
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic  --no-input
python manage.py createsuperuser
```
