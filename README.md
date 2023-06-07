# FOODGRAM

Приложение «Продуктовый помощник»: сайт, на котором пользователи будут публиковать рецепты, добавлять чужие рецепты в избранное и подписываться на публикации других авторов. Сервис «Список покупок» позволит пользователям создавать список продуктов, которые нужно купить для приготовления выбранных блюд.

Проект доступен по адресу: http://51.250.71.93/

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
git clone https://github.com/mishatar/foodgram-project-react.git
```
- Для работы с проектом на сервере необходимо установить Docker и Docker-compose:

```commandline
sudo apt install docker.io 
```

- Скопировать на сервер файлы docker-compose.yml, default.conf из папки infra (команды выполнять находясь в папке infra):
```commandline
scp docker-compose.yml default.conf username@IP:/home/username/   # username - имя пользователя на сервере
                                                                  # IP - публичный IP сервера
```

- Для работы с GitHub Actions необходимо в репозитории в разделе Secrets > Actions создать переменные окружения:
```commandline
SECRET_KEY              # секретный ключ Django проекта
DOCKER_PASSWORD         # пароль от Docker Hub
DOCKER_USERNAME         # логин Docker Hub
HOST                    # публичный IP сервера
USER                    # имя пользователя на сервере
SSH_KEY                 # приватный ssh-ключ
TELEGRAM_TO             # ID телеграм-аккаунта для посылки сообщения
TELEGRAM_TOKEN          # токен бота, посылающего сообщение

DB_ENGINE               # django.db.backends.postgresql
DB_NAME                 # postgres
POSTGRES_USER           # postgres
POSTGRES_PASSWORD       # postgres
DB_HOST                 # db
DB_PORT                 # 5432 (порт по умолчанию)
```

- Создать и запустить контейнеры Docker, выполнить команду на сервере (версии команд "docker compose" или "docker-compose" отличаются в зависимости от установленной версии Docker Compose):
```
sudo docker compose up -d
```

- После успешной сборки выполнить миграции:
```
sudo docker compose exec web python manage.py migrate
```

- Создать суперпользователя:
```
sudo docker compose exec backend python manage.py createsuperuser
```

- Собрать статику:
```
sudo docker compose exec backend python manage.py collectstatic --noinput
```

- Наполнить базу данных содержимым из файлов:
```
sudo docker compose exec web python manage.py load_ingredients
sudo docker compose exec web python manage.py load_tags
```

### После каждого обновления репозитория (push в ветку master) будет происходить:
- Проверка кода на соответствие стандарту PEP8 (с помощью пакета flake8)
- Сборка и доставка докер-образов frontend и backend на Docker Hub
- Разворачивание проекта на удаленном сервере
- Отправка сообщения в Telegram в случае успеха