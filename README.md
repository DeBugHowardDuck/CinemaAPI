# CinemaAPI - REST API для каталога фильмов

[![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0-green.svg)](https://flask.palletsprojects.com)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red.svg)](https://sqlalchemy.org)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Современный REST API для управления каталогом фильмов, построенный на Flask. Включает JWT аутентификацию, расширенную фильтрацию, пагинацию и полную документацию Swagger.

## Основные возможности

### Аутентификация и безопасность
- JWT-аутентификация с безопасной генерацией токенов
- Хеширование паролей с использованием Werkzeug
- Защищенные endpoints для операций изменения данных

### Управление фильмами
- Полный CRUD для фильмов
- Расширенная фильтрация по жанру, режиссеру, году
- Умный поиск по названию
- Гибкая сортировка по любому полю
- Пагинация с настраиваемым размером страницы

### Управление данными
- Справочники жанров и режиссеров
- Система избранных фильмов пользователей
- Реляционная модель базы данных с внешними ключами
- Валидация данных с помощью Marshmallow

### Документация и тестирование
- Интерактивный Swagger UI на корневом endpoint
- Полный набор тестов с pytest
- Автогенерируемая документация API
- Health check endpoint для мониторинга

## Технологический стек

| Компонент | Технология | Назначение |
|-----------|------------|------------|
| **Backend** | Flask 3.0 | Веб-фреймворк |
| **API** | Flask-RESTX | REST API с автодокументацией |
| **База данных** | SQLAlchemy 2.0 | ORM и управление БД |
| **Валидация** | Marshmallow | Сериализация и валидация данных |
| **Аутентификация** | PyJWT | Обработка JWT токенов |
| **Тестирование** | pytest | Фреймворк тестирования |
| **База данных** | SQLite | База данных для разработки |

## Быстрый старт

### Требования
- Python 3.12+
- pip (менеджер пакетов Python)

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/DeBugHowardDuck/CinemaAPI.git
cd CinemaAPI
```

2. **Создайте виртуальное окружение**
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

3. **Установите зависимости**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

4. **Настройте переменные окружения**
```bash
# Создайте файл .env
echo "DATABASE_URI=sqlite:///./instance/cinema.db" > .env
echo "JWT_SECRET=your-super-secret-jwt-key" >> .env
```

5. **Запустите приложение**
```bash
python run.py
```

6. **Доступ к API**
- **Swagger UI**: http://127.0.0.1:5000/
- **API Base**: http://127.0.0.1:5000/api/

## API Endpoints

### Аутентификация
| Метод | Endpoint | Описание | Требуется авторизация |
|-------|----------|----------|----------------------|
| `POST` | `/auth/register` | Регистрация нового пользователя | Нет |
| `POST` | `/auth/login` | Вход пользователя | Нет |

### Фильмы
| Метод | Endpoint | Описание | Требуется авторизация |
|-------|----------|----------|----------------------|
| `GET` | `/movies` | Список фильмов (с фильтрами) | Нет |
| `GET` | `/movies/{id}` | Получить фильм по ID | Нет |
| `POST` | `/movies` | Создать новый фильм | Да |
| `PUT` | `/movies/{id}` | Обновить фильм | Да |
| `DELETE` | `/movies/{id}` | Удалить фильм | Да |

### Жанры и режиссеры
| Метод | Endpoint | Описание | Требуется авторизация |
|-------|----------|----------|----------------------|
| `GET` | `/genres` | Список всех жанров | Нет |
| `POST` | `/genres` | Создать новый жанр | Да |
| `GET` | `/directors` | Список всех режиссеров | Нет |
| `POST` | `/directors` | Создать нового режиссера | Да |

### Избранные фильмы
| Метод | Endpoint | Описание | Требуется авторизация |
|-------|----------|----------|----------------------|
| `POST` | `/favorites/{user_id}/{movie_id}` | Добавить в избранное | Да |
| `DELETE` | `/favorites/{user_id}/{movie_id}` | Удалить из избранного | Да |

## Расширенные возможности

### Фильтрация и поиск фильмов
```bash
# Фильтр по жанру и году
GET /movies?genre_id=1&year=2020

# Поиск по названию
GET /movies?search=avengers

# Сортировка по рейтингу (по убыванию)
GET /movies?sort=rating&order=desc

# Пагинация
GET /movies?page=2&per_page=10

# Комбинированные фильтры
GET /movies?genre_id=1&year=2020&sort=rating&order=desc&page=1&per_page=20
```

### Пример аутентификации
```bash
# Регистрация пользователя
curl -X POST http://127.0.0.1:5000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"secure123","name":"Иван Иванов"}'

# Вход в систему
curl -X POST http://127.0.0.1:5000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"secure123"}'

# Использование токена для защищенных endpoints
curl -X POST http://127.0.0.1:5000/movies \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer YOUR_JWT_TOKEN" \
  -d '{"title":"Начало","year":2010,"rating":8.8,"genre_id":1,"director_id":1}'
```

## Тестирование

Запуск тестов:
```bash
# Запустить все тесты
pytest

# Запуск с подробным выводом
pytest -v

# Запуск конкретного файла тестов
pytest tests/test_movies.py
```

## Структура проекта

```
CinemaAPI/
├── app/
│   ├── models/          # Модели базы данных
│   │   ├── movie.py     # Модель фильма
│   │   ├── user.py      # Модель пользователя
│   │   ├── genre.py     # Модель жанра
│   │   ├── director.py  # Модель режиссера
│   │   └── favorite.py  # Связь избранных
│   ├── views/           # API endpoints
│   │   ├── movies.py    # Endpoints фильмов
│   │   ├── auth.py      # Аутентификация
│   │   ├── genres.py    # Endpoints жанров
│   │   ├── directors.py # Endpoints режиссеров
│   │   ├── favorites.py # Endpoints избранных
│   │   ├── user.py      # Endpoints пользователей
│   │   └── health.py    # Health check
│   ├── schemas/         # Схемы валидации данных
│   ├── utils/           # Утилиты
│   │   ├── auth.py      # Декораторы аутентификации
│   │   ├── jwt_helper.py # JWT утилиты
│   │   ├── error_handlers.py # Обработка ошибок
│   │   └── logger.py    # Конфигурация логирования
│   └── extensions/      # Расширения Flask
├── tests/               # Набор тестов
├── config.py           # Конфигурация
├── run.py              # Точка входа приложения
└── requirements.txt    # Зависимости
```

## Конфигурация

### Переменные окружения
| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| `DATABASE_URI` | Строка подключения к БД | `sqlite:///C:/kinobaza_data/instance/kinobaza.db` |
| `JWT_SECRET` | Секретный ключ для JWT токенов | `dev-secret` |

### База данных
- **Разработка**: SQLite (файловая)
- **Продакшн**: PostgreSQL/MySQL (настраивается через `DATABASE_URI`)

## Развертывание

### Разработка
```bash
python run.py
```

### Продакшн
```bash
# Используя Gunicorn
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```