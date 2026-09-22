hello everyone who check this file and this project!
what about this project? what this project will be do? - that a Cinema booking service with booking placement to watch movies

am looking in this project like first strike attempt to learn python and all technologies
what me will neeed to get a job

my friend said me
"do ur project without any knowleadge and do problems when its get up that will be better than stay on one place"
and they send me a seed of thinking on my mind about it i was think really i must do what they are say me they might be right
and now after some mounths i getting up to do it welp lets start

why am actually want learn from this project there is answer:

- FastAPI
- Pydantic v2 (rust based version)
- SQLAlchemy
- PostgreSQL
- SQL
- JWT
- Docker and Docker.compose
- PyTest
- Asyncio (FastAPI)
- Async (python)
- Alembic
- Structure of fastapi project

and lets talk about structure FastAPI project
they will be look might be like that

my_fastapi_project/
├── alembic/ # Миграции базы данных (если используется Alembic)
├── src/ # Исходный код приложения
│ ├── api/ # Роутеры (эндпоинты), работа с HTTP
│ │ ├── v1/
│ │ │ ├── endpoints/
│ │ │ │ ├── auth.py
│ │ │ │ ├── users.py
│ │ │ │ └── items.py
│ │ │ └── api.py # Объединение всех роутеров v1
│ │ └── deps.py # Общие зависимости (get_db, get_current_user и т.д.)
│ │
│ ├── core/ # Конфигурация и базовые настройки
│ │ ├── config.py # Pydantic Settings (чтение .env)
│ │ ├── database.py # Подключение к БД, сессия (SQLAlchemy / Tortoise)
│ │ └── security.py # Хеширование паролей, JWT-токены
│ │
│ ├── models/ # ORM-модели (например, SQLAlchemy модели для БД)
│ │ ├── user.py
│ │ └── item.py
│ │
│ ├── schemas/ # Pydantic-модели (валидация данных, вход/выход)
│ │ ├── user.py
│ │ └── item.py
│ │
│ ├── services/ # Бизнес-логика (сервисный слой)
│ │ ├── user_service.py
│ │ └── item_service.py
│ │
│ ├── crud/ # Запросы к базе данных (Repository pattern)
│ │ ├── crud_user.py
│ │ └── crud_item.py
│ │
│ └── main.py # Точка входа, инициализация FastAPI
│
├── tests/ # Автоматические тесты (pytest)
│ ├── conftest.py
│ ├── test_auth.py
│ └── test_users.py
│
├── .env # Переменные окружения (секреты, настройки)
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
