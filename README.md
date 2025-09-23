📝 Blog API  
REST API для блога с поддержкой постов, категорий, комментариев и JWT-аутентификации.  
Реализован на Django + Django REST Framework с документацией Swagger.  


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
