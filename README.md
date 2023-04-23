### Описание проекта:

Yatube - это социальная сеть для блогеров.
Возможности:
- размещение своего поста;
- добавление картинки к тексту;
- чтение постов других авторов;
- присваивание группы своему посту;
- подписки на других авторов. 

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Svetlana-Zimina/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов к API:

Получение списка всех публикаций/Создание публикации:

```
GET/POST

http://127.0.0.1:8000/api/v1/posts/
```

Получение/Обновление/Частичное обновление/Удаление публикации:

```
GET/PUT/PATCH/DELETE

http://127.0.0.1:8000/api/v1/posts/{id}/
```

Получение списка сообществ:

```
GET

http://127.0.0.1:8000/api/v1/groups/
```

Получение информации о сообществе:

```
GET

http://127.0.0.1:8000/api/v1/groups/{id}/
```

Получение списка комментариев/Создание комментариев к посту:

```
GET/POST

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

Получение/Обновление/Частичное обновление/Удаление комментария к посту:

```
GET/PUT/PATCH/DELETE

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

Получение подписок/Создание подписки:

```
GET/POST

http://127.0.0.1:8000/api/v1/follow/
```

Получение JWT-токена:

```
POST

http://127.0.0.1:8000/api/v1/jwt/create/
```

Обновление JWT-токена:

```
POST

http://127.0.0.1:8000/api/v1/jwt/refresh/
```

Проверка JWT-токена:

```
POST

http://127.0.0.1:8000/api/v1/jwt/verify/
```

### Технологии:

- Django Framework;
- Django Rest Framework.

### Над проектом работали:

Зимина Светлана
https://github.com/Svetlana-Zimina