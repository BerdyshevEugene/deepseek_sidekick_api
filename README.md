# 🤖 DeepSeek Sidekick API

[![Python](https://img.shields.io/badge/Python-3.13-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.123+-green.svg)](https://fastapi.tiangolo.com)
[![UV](https://img.shields.io/badge/UV-Package%20Manager-orange.svg)](https://astral.sh)
[![SQLite](https://img.shields.io/badge/SQLite-Database-lightgrey.svg)](https://sqlite.org)

> Простой API для взаимодействия с моделью DeepSeek, с сохранением истории запросов в SQLite базу данных.

## 🚀 Быстрый старт

### Локальная установка
```bash
git clone <repository-url>
cd deepseek_sidekick_api
uv sync
cp .env.example .env  # И настройте ваш DEEPSEEK_API_KEY
uv run uvicorn main:app --reload
```

## 📋 Требования

- **Python 3.13+**
- **UV** (менеджер пакетов)
- **DeepSeek API Key** (получите на https://platform.deepseek.com/)

## 🏗️ Структура проекта

```
deepseek_sidekick_api/
├── 📦 pyproject.toml          # Конфигурация проекта и зависимости
├── 📦 uv.lock                 # Файл блокировки зависимостей
├── 🔧 main.py                 # Основное FastAPI приложение
├── 🔧 db.py                   # Модели базы данных и функции работы с ней
├── 🔧 config.py               # Конфигурация приложения
├── 🔧 deepseek_client.py      # Клиент для работы с DeepSeek API
├── 📝 .env.example            # Пример переменных окружения
├── 🗃️ data.db                # SQLite база данных (создается автоматически)
```

## 🛠️ Основные эндпоинты

### POST `/requests` - Отправить запрос в DeepSeek
Отправляет ваш запрос в модель DeepSeek и возвращает ответ.

```bash
curl -X POST "http://localhost:8000/requests" \
     -H "Content-Type: application/json" \
     -d '{"prompt": "Привет, как дела?"}'
```

### GET `/requests` - Получить историю запросов
Возвращает историю всех запросов текущего пользователя (по IP адресу).

```bash
curl -X GET "http://localhost:8000/requests"
```

## 📦 Управление зависимостями с UV

### Установка UV
```bash
# macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Основные команды UV
```bash
uv sync               # Синхронизировать зависимости
uv add package        # Добавить пакет
uv remove package     # Удалить пакет
uv run command        # Запустить команду в окружении
```

## 🔧 Конфигурация

### Переменные окружения
Создайте файл `.env` на основе `.env.example`:

```bash
DEEPSEEK_API_KEY=your-api-key-here
```

## 🗃️ База данных

Проект использует SQLite для хранения истории запросов:

**Структура таблицы `chat_requests`:**
- `id` - уникальный идентификатор записи
- `ip_address` - IP адрес пользователя
- `prompt` - текст запроса пользователя
- `response` - ответ от модели DeepSeek

База данных создается автоматически при запуске приложения.

## 🤝 Участие в разработке

1. Форкните репозиторий
2. Создайте ветку для функции: `git checkout -b feature/amazing-feature`
3. Зафиксируйте изменения: `git commit -m 'Add amazing feature'`
4. Отправьте в ветку: `git push origin feature/amazing-feature`
5. Создайте Pull Request

## 🔗 Полезные ссылки

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [UV Documentation](https://docs.astral.sh/uv/)
- [DeepSeek Platform](https://platform.deepseek.com/)
- [SQLite Documentation](https://www.sqlite.org/docs.html)

## 📄 Лицензия

Этот проект лицензирован под MIT License - см. файл [LICENSE](LICENSE) для деталей.