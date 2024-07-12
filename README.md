# 📁 Mem API

## 📖 Кратко о проекте
Этот проект представляет собой веб-приложение на Python, использующее 
FastAPI для предоставления API для работы с коллекцией мемов. Приложение 
разделено на два сервиса: сервис с публичным API для бизнес-логики мемов 
и сервис для работы с медиа-файлами, использующий S3-совместимое хранилище 
(MinIO).

---

## 🧾 TODO список (основные положения)
- [x] Настроить инициализацию проекта FastAPI с использованием Uvicorn для 
асинхронной обработки запросов.
- [x] Создать модели SQLAlchemy для данных мемов и медиа-файлов.
- [x] Использовать Alembic для управления миграциями базы данных PostgreSQL.
- [x] Реализовать CRUD операции для мемов:
- [x] Реализовать интеграцию с сервисом для работы с медиа-файлами (MinIO)
- [x] Написать unit-тесты для основной функциональности
- [x] Документирование API с использованием Swagger/OpenAPI.
- [x] Создать Docker Compose файл для локального запуска проекта.
- [x] Написать README.md с инструкциями по запуску проекта и описанием 
функциональности.

---

## 💻 Запуск проекта
Клонирование репозитория:
```bash
git clone https://github.com/SamvelMhitaryan/mad.git
cd madsoft
```

Создание виртуального окружения (venv):
```bash
python -m venv venv
```

Активация виртуального окружения (venv):
Linux / Mac
```bash
source venv/bin/activate
```

Windows
```bash
venv\Scripts\activate
```

Установка зависимостей:
```bash
pip install -r requirements.txt
```

Настройка переменных окружения:
Создайте файл .env на основе .env.example и укажите необходимые значения, 
такие как настройки подключения к базе данных PostgreSQL и настройки для 
подключения к MinIO.

Запуск проекта с помощью docker-compose:

```bash
docker compose up
```

Приложение будет доступно по адресу http://localhost:8000.

## Дополнительная информация
Документация API доступна по адресу http://localhost:8000/docs, где вы можете
ознакомиться с доступными эндпоинтами и их параметрами.
Для остановки сервера нажмите Ctrl + C в консоли.