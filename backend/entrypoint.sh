#!/bin/bash
set -e

echo "➡️ Генерируем миграции..."
python manage.py makemigrations --noinput

echo "➡️ Применяем миграции..."
python manage.py migrate --noinput

echo "➡️ Собираем статику..."
python manage.py collectstatic --noinput

echo "🚀 Запускаем сервер..."
python manage.py runserver 0.0.0.0:8000


