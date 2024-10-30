# Currency Rate Tracker
## Описание проекта
 Проект Currency Rate Tracker представляет собой Django-приложение для отслеживания текущего курса доллара к рублю и хранения истории изменений. Приложение автоматически обновляет данные каждые 10 секунд и отображает последние 10 записей по курсу.

## Установка
1. Клонируйте репозиторий:
    ```bash
   git clone git@github.com:Dontgoingforyou/currency_project.git
   cd currency_project

2. Установите зависимости:
    ```bash
   poetry install
   
3. Примените миграции для инициализации базы данных:
    ```bash
   python manage.py migrate
   
## Запуск
1. Запустите сервер Django:
    ```bash
   python manage.py runserver

2. Запустите фоновую задачу для обработки обновлений курса:
    ```bash
   python manage.py process_tasks

## API
- GET /get-current-usd/ — возвращает JSON с историей последних 10 записей по курсу доллара к рублю.

## Пример ответа API
    {
    "history": [
    {
      "rate": "97.3500",
      "timestamp": "2024-10-30T13:14:26.022Z"
    },
        ...
        ]
    }

## Зависимости
Проект использует следующие основные зависимости:

- Django
- requests
- Django Background Tasks