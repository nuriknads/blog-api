📝 Blog API  
REST API для блога с поддержкой постов, категорий, комментариев и JWT-аутентификации.  
Реализован на Django + Django REST Framework с документацией Swagger.  

## 📌 Функционал:
- Управление постами (CRUD)
- Категории и теги
- Система комментариев
- JWT-аутентификация
- Swagger-документация API

## 🚀 Стек технологий:
- Python 3.x
- Django 4.x
- Django REST Framework
- Simple JWT
- drf-spectacular (Swagger Docs)
- SQLite (по умолчанию)

## 🔗 Примеры эндпоинтов:
GET /api/posts/ — список постов  
POST /api/posts/ — создать пост  
GET /api/categories/ — список категорий  
POST /api/token/ — JWT-токен  

## ▶ Запуск проекта:
```bash
git clone https://github.com/nuriknads/blog-api.git
cd blog-api
python -m venv venv
source venv/bin/activate  # (Linux/Mac)
venv\Scripts\activate     # (Windows)
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
