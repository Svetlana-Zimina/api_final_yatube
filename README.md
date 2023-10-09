## Описание проекта:

Yatube - это социальная сеть для блогеров.
Возможности:
- размещение своего поста;
- добавление картинки к тексту;
- чтение постов других авторов;
- присваивание группы своему посту;
- подписки на других авторов;
- реализована регистрация и аутентификация пользователей.

Проект создан для тренировки написания API следуя техническому заданию - документации API. Документация предоставляется в формате Redoc.

## Как запустить проект:

1. ### Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Svetlana-Zimina/api_final_yatube.git
```

```
cd api_final_yatube
```

2. ### Cоздать и активировать виртуальное окружение:

```
python -m venv env
source venv/Scripts/activate
python -m pip install --upgrade pip
```

3. ### Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. ### Выполнить миграции:

```
python manage.py migrate
```

5. ### Запустить проект:

```
python manage.py runserver
```

После запуска сервера документация API будет доступна по [адресу](http://127.0.0.1:8000/redoc/)

## Примеры запросов к API:

1. ### Получение списка всех публикаций/Создание публикации:

```
GET/POST

http://127.0.0.1:8000/api/v1/posts/
```

2. ### Получение/Обновление/Частичное обновление/Удаление публикации:

```
GET/PUT/PATCH/DELETE

http://127.0.0.1:8000/api/v1/posts/{id}/
```

3. ### Получение списка сообществ:

```
GET

http://127.0.0.1:8000/api/v1/groups/
```

4. ### Получение информации о сообществе:

```
GET

http://127.0.0.1:8000/api/v1/groups/{id}/
```

5. ### Получение списка комментариев/Создание комментариев к посту:

```
GET/POST

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/
```

6. ### Получение/Обновление/Частичное обновление/Удаление комментария к посту:

```
GET/PUT/PATCH/DELETE

http://127.0.0.1:8000/api/v1/posts/{post_id}/comments/{id}/
```

7. ### Получение подписок/Создание подписки:

```
GET/POST

http://127.0.0.1:8000/api/v1/follow/
```

8. ### Получение JWT-токена:

```
POST

http://127.0.0.1:8000/api/v1/jwt/create/
```

9. ### Обновление JWT-токена:

```
POST

http://127.0.0.1:8000/api/v1/jwt/refresh/
```

10. ### Проверка JWT-токена:

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