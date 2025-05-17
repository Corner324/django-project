# 🐾 Dog API

Полнофункциональный Django REST API для работы c породами и собаками.

Проект демонстрирует:

* чистую архитектуру Django + DRF;
* «ленивые» аннотации через `Subquery` / `OuterRef` без N+1‑запросов;
* контейнеризацию (Docker + PostgreSQL);
* строгий стиль кода (PEP 8 + ruff) и доскональные docstrings в формате Google.

---

## ⚡ Быстрый старт

```bash
git clone https://github.com/Corner324/django-project.git
cd django-project/backend

# создаём .env из шаблона
cp .env.example .env

# собрать и запустить stack
docker compose -f docker/docker-compose.yml up --build
```

```
API  : http://localhost:8000/api/
Admin: http://localhost:8000/admin/  (создайте супер‑юзера)
```

---

## 🗂️ Структура репозитория

```
backend/
├── apps/                # «фичевые» приложения
│   └── dogs/            # модели Dog / Breed + сериализаторы + ViewSets
├── config/              # настройки проекта (settings / urls / wsgi / asgi)
├── docker/              # Dockerfile и docker‑compose.yml
├── entrypoint.sh        # миграции + collectstatic + runserver
├── requirements.txt     # все зависимости c фиксированными версиями
└── .env(.example)       # конфиденциальные переменные окружения
```

Полный обзор директорий см. в шапке README.

---

## 🚀 Функциональность API

| HTTP   | Маршрут        | Описание                                                  | Доп. поля в ответе |
| ------ | --------------------- | ----------------------------------------------------------------- | --------------------------------- |
| GET    | `/api/dogs/`        | Список всех собак                                  | `average_age_for_breed`         |
| POST   | `/api/dogs/`        | Создать собаку (указать `breed`по ID)    | —                                |
| GET    | `/api/dogs/{id}/`   | Детали собаки                                         | `same_breed_count`              |
| PUT    | `/api/dogs/{id}/`   | Обновить собаку                                     | —                                |
| DELETE | `/api/dogs/{id}/`   | Удалить собаку                                       | —                                |
| GET    | `/api/breeds/`      | Список пород                                           | `dog_count`                     |
| POST   | `/api/breeds/`      | Создать породу                                       | —                                |
| CRUD   | `/api/breeds/{id}/` | Получить / изменить / удалить породу | —                                |

```http
POST /api/dogs/
{
  "name": "Бобик",
  "age": 2,
  "breed": 1,
  "gender": "Самец",
  "color": "рыжий",
  "favorite_food": "кость",
  "favorite_toy": "мячик"
}
```

---

## 🧠 Подзапросы без N+1

* **/dogs/** — `average_age_for_breed` считается подзапросом

  `Subquery(Dog.objects.filter(breed=OuterRef('breed')).aggregate(Avg('age')))`
* **/dogs/{id}** — `same_breed_count` аналогично через `Count`
* **/breeds/** — `dog_count` = `Breed.objects.annotate(Count('dog'))`

Все вычисляется в одном SQL‑запросе на эндпоинт.

---

## 🛠️ Разработка

| Команда                                                  | Действие                            |
| --------------------------------------------------------------- | ------------------------------------------- |
| `ruff check .`                                                | Линт кода                           |
| `ruff check . --fix`                                          | Авто‑исправление стиля |
| `docker compose exec backend python manage.py makemigrations` | Создать миграции             |

Максимальная длина строки — 119 симв.

Все функции и классы документированы docstring‑ами (Google Style).

---

## 🔐 Переменные окружения (`.env.example`)

| Переменная                                    | Значение по умолчанию        | Описание                                       |
| ------------------------------------------------------- | ----------------------------------------------- | ------------------------------------------------------ |
| `DJANGO_DEBUG`                                        | `True`                                        | Режим отладки                              |
| `DJANGO_SECRET_KEY`                                   | `replace‑me`                                 | Секретный ключ                            |
| `DATABASE_URL`                                        | `postgres://user:pass@db:5432/django_project` | Подключение к PostgreSQL                   |
| `ALLOWED_HOSTS`                                       | `127.0.0.1,localhost`                         | Список разрешённых хостов       |
| `POSTGRES_USER`/`POSTGRES_PASSWORD`/`POSTGRES_DB` | —                                              | Конфигурация контейнера базы |

---

## 🐳 Docker

```bash
# сборка backend‑образа
docker build -t dog-api-backend -f docker/Dockerfile ..

# старт через compose
docker compose -f docker/docker-compose.yml up
```

* `entrypoint.sh` автоматически применит миграции, соберёт статику и запустит сервер.
* Образы Python + PostgreSQL 14.

---

## 📝 Коммит‑модель

* Работа ведётся в ветках `feature/*`.
* PR → review → merge в `main`.
