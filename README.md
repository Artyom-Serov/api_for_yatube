# API для социальной сети YaTube.

Социальная сеть с возможностью регистрации и ведения своего блога. Посты могут содержать изображения и текст. Также они могут быть объединены в сообщества. Есть возможность подписаться на автора, прокомментировать пост, вступить в сообщество, читать общую ленту сайта или ленту своих подписок.
<br />*Позволяет делать запросы к моделям проекта: Посты, Группы, Комментарии, Подписки. Поддерживает методы GET, POST, PUT, PATCH, DELETE Предоставляет данные в формате JSON*

## Технологии:

- [Python 3.9](https://www.django-rest-framework.org/)
- [Django REST Framework 3.12.4](https://www.django-rest-framework.org/)
- [Django 2.2.16](https://www.djangoproject.com/)
- [Djangorestframework-simplejwt 4.7.2](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/)
- [Pillow 8.3.1](https://pillow.readthedocs.io/en/stable/index.html)
## Как запустить проект: 
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Artyom-Serov/api_yatube.git
```
```
cd api_yatube
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
```
```
source venv/bin/activate
```
```
python3 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```
Выполнить миграции:

```
python3 manage.py migrate
```
Запустить проект:
```
python3 manage.py runserver
```
