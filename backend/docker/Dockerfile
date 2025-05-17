FROM python:3.12-slim-bookworm

# Обновляем pip и создаём виртуальное окружение
ENV VIRTUAL_ENV=/venv
RUN python -m venv $VIRTUAL_ENV && \
    $VIRTUAL_ENV/bin/pip install --upgrade pip

# Добавляем виртуальное окружение в PATH
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект
COPY . .

# Копируем и настраиваем entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

# Запускаем сервер по умолчанию
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
