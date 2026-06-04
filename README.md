# AI Growth Infrastructure System

![Python](https://img.shields.io/badge/Python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-teal)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Redis](https://img.shields.io/badge/Redis-Queue-red)
![Celery](https://img.shields.io/badge/Celery-Workers-green)
![React](https://img.shields.io/badge/React-Admin%20Dashboard-61DAFB)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-blue)
![Docker](https://img.shields.io/badge/Docker-Compose-2496ED)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

AI-инфраструктура для автоматизации B2B-продаж, поиска клиентов, рыночной аналитики, генерации контента, подготовки коммерческих предложений и управления CRM-пайплайном.

Проект представляет собой прототип продуктовой AI-системы, которая объединяет backend API, базу данных, очередь задач, Telegram-бота, React dashboard и несколько AI-модулей для роста B2B-бизнеса.

---

## О проекте

* поиск потенциальных клиентов;
* нормализацию и дедупликацию лидов;
* оценку качества лидов;
* генерацию outreach-сообщений;
* подготовку коммерческих предложений;
* мониторинг рыночных сигналов;
* генерацию контент-планов и материалов;
* аналитику CRM-пайплайна;
* уведомления через Telegram;
* управление через admin dashboard.

---

## Основные модули

### Lead Hunter AI

Модуль поиска потенциальных клиентов.

Функции:

* поиск компаний по запросу и региону;
* сбор лидов из разных источников;
* нормализация данных;
* дедупликация;
* расчёт lead score;
* сохранение лидов в CRM-базу.

### Outreach AI

Модуль генерации персонализированных сообщений.

Функции:

* создание outreach-кампаний;
* генерация последовательности сообщений;
* поддержка разных каналов коммуникации;
* сохранение сообщений как черновиков;
* подготовка лидов к дальнейшей обработке.

### Market Intelligence AI

Модуль анализа рыночных сигналов.

Функции:

* создание market watch;
* мониторинг ниш и регионов;
* поиск рыночных возможностей;
* расчёт opportunity score;
* вывод top-сигналов для команды.

### Content AI Engine

Модуль генерации контента.

Функции:

* генерация тем;
* создание контент-планов;
* подготовка текстов для выбранной аудитории;
* хранение материалов в статусе draft.

### Proposal & Sales AI

Модуль подготовки коммерческих предложений.

Функции:

* генерация proposal по конкретному лиду;
* учёт компании, типа предложения и модели оплаты;
* сохранение предложения;
* обновление статуса лида.

### CRM Brain & Analytics

Аналитический модуль CRM.

Функции:

* сводка по пайплайну;
* рекомендации по лидам;
* управленческий AI-отчёт;
* анализ статусов и потенциальных возможностей.

### Telegram Bot

Telegram-бот используется как дополнительный интерфейс для уведомлений и управления системой.

### Admin Dashboard

React dashboard предоставляет визуальный интерфейс для просмотра лидов, рыночных сигналов и сводки по пайплайну.

---


## Технологический стек

### Backend

* Python
* FastAPI
* SQLAlchemy
* Pydantic
* PostgreSQL
* Redis
* Celery

### AI / Automation

* AI gateway
* OpenAI-compatible provider logic
* Lead scoring
* Content generation
* Proposal generation
* Market intelligence
* CRM recommendations

### Frontend

* React
* Vite
* CSS
* REST API integration

### Telegram

* Telegram Bot API
* Bot handlers
* Keyboards
* Backend API client

### Infrastructure

* Docker
* Docker Compose
* Environment variables
* Multi-service architecture

---

## API endpoints

### Leads

```http
GET /leads/
POST /leads/hunt
PATCH /leads/{lead_id}/status
```

### Outreach

```http
POST /outreach/campaigns
GET /outreach/campaigns
POST /outreach/sequence/generate
GET /outreach/sequences
```

### Market Intelligence

```http
POST /market/watches
GET /market/watches
POST /market/watches/{watch_id}/run
GET /market/signals
GET /market/signals/top
```

### Content AI

```http
POST /content/plans
GET /content/plans
POST /content/generate
GET /content/items
```

### Proposals

```http
POST /proposals/generate
GET /proposals/
PATCH /proposals/{proposal_id}/status
```

### Analytics

```http
GET /analytics/summary
GET /analytics/recommendations
GET /analytics/management-report
```

---

## Пример запроса Lead Hunter

```http
POST /leads/hunt
Content-Type: application/json

{
  "query": "AI software automation outsourcing",
  "region": "USA",
  "limit_per_source": 5
}
```

Пример ответа:

```json
[
  {
    "id": 1,
    "title": "AI Automation Company",
    "region": "USA",
    "score": 82,
    "status": "new"
  }
]
```

---

## Пример генерации outreach sequence

```http
POST /outreach/sequence/generate
Content-Type: application/json

{
  "campaign_id": 1,
  "lead_id": 1,
  "channel": "email",
  "steps": 3
}
```

---

## Автор

**Алексей Молокин**
AI Engineer / Python Developer

GitHub: [molokinaleksej5](https://github.com/molokinaleksej5)
