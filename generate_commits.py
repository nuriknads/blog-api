import os
import subprocess
from datetime import datetime, timedelta
import random

# ✅ Настройки
start_date = datetime(2020, 3, 1, 10, 0, 0)
end_date = datetime(2021, 1, 31, 18, 0, 0)
num_commits = 70

# ✅ Пример сообщений
messages = [
    "Initial project setup",
    "Add Django project structure",
    "Configure settings and apps",
    "Create Post model",
    "Add Post serializer",
    "Implement Post CRUD API",
    "Add JWT authentication",
    "Configure DRF permissions",
    "Add pagination and filtering",
    "Create Category model",
    "Implement Category API",
    "Add Comment model and API",
    "Write tests for Post API",
    "Write tests for Comment API",
    "Fix authentication bug",
    "Improve Swagger documentation",
    "Add user registration endpoint",
    "Refactor views for clarity",
    "Optimize database queries",
    "Update requirements.txt",
    "Add Dockerfile",
    "Configure docker-compose",
    "Setup Celery for async tasks",
    "Add email notifications",
    "Fix pagination issue",
    "Improve API performance",
    "Add custom permissions",
    "Add search and ordering filters",
    "Write more unit tests",
    "Update README.md",
    "Add .gitignore",
    "Fix JWT refresh bug",
    "Implement token blacklist",
    "Improve error handling",
    "Update API docs",
    "Add logging configuration",
    "Refactor serializers",
    "Add admin customization",
    "Implement user profile API",
    "Add signal for post save",
    "Fix category filtering",
    "Refactor comment logic",
    "Add test coverage report",
    "Improve Celery configuration",
    "Add Redis integration",
    "Fix minor bugs",
    "Improve code formatting",
    "Update Swagger UI",
    "Add deployment configs",
    "Final bug fixes",
    "Prepare for production",
]

# ✅ Генерация случайных дат в диапазоне
delta = (end_date - start_date).days
dates = [start_date + timedelta(days=random.randint(0, delta), hours=random.randint(8, 20)) for _ in range(num_commits)]
dates.sort()

# ✅ Генерация коммитов
for i in range(num_commits):
    commit_date = dates[i].strftime('%Y-%m-%d %H:%M:%S')
    message = random.choice(messages)
    
    # Создаем пустой коммит с датой
    subprocess.run([
        'git', 'commit', '--allow-empty', '--date', commit_date, '-m', message
    ])
    print(f"✅ Commit {i+1}/{num_commits}: {message} ({commit_date})")

print("🎉 Все коммиты сгенерированы!")
