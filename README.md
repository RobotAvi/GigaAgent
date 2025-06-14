# GigaAgent AI Agents

Проект для работы с GigaChat API через различные инструменты и агентов.

## Текущий статус

- [x] Шаг 1: Проверка соединения с GigaChat API
- [x] Шаг 2: Интеграция с поисковым инструментом DuckDuckGo
  - Создан агент с возможностью поиска через DuckDuckGo
  - Агент может отвечать на вопросы, используя актуальную информацию из интернета
  - Реализовано корректное закрытие соединения с API
- [x] Шаг 3: Работа с файловой системой
  - Создан агент с возможностью управления файлами
  - Реализована работа с Python REPL
  - Агент может создавать и редактировать файлы
  - Поддерживается выполнение Python кода

## Следующие шаги

- [ ] Будут определены позже

## Структура проекта

```
GigaAgent/
├── Step1_testGigachat/     # Базовый тест GigaChat
│   ├── giga_step001.py     # Основной скрипт
│   ├── config.py           # Конфигурация
│   └── giga_step001_test.py # Тесты
├── Step2_use_search_tool/  # Поиск с DuckDuckGo
│   ├── giga_step002.py     # Основной скрипт
│   ├── config.py           # Конфигурация
│   └── giga_step002_test.py # Тесты
├── Step3_create_python_hello_world_with_agent/ # Работа с файлами
│   ├── giga_step003.py     # Основной скрипт
│   └── config.py           # Конфигурация
├── requirements.txt        # Зависимости
└── .gitignore             # Игнорируемые файлы
```

## Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourusername/GigaAgent.git
cd GigaAgent
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл конфигурации:
```bash
cp Step1_testGigachat/config.template.py Step1_testGigachat/config.py
cp Step2_use_search_tool/config.template.py Step2_use_search_tool/config.py
```

5. Отредактируйте файлы конфигурации и добавьте ваш API ключ GigaChat:
```python
GIGACHAT_CREDENTIALS = "your_api_key_here"
```

## Использование

### Шаг 1: Базовый тест GigaChat
```bash
python Step1_testGigachat/giga_step001.py
```

### Шаг 2: Поиск с DuckDuckGo
```bash
python Step2_use_search_tool/giga_step002.py
```

### Шаг 3: Работа с файловой системой
```bash
python Step3_create_python_hello_world_with_agent/giga_step003.py
```

## Разработка

### Запуск тестов
```bash
pytest Step1_testGigachat/giga_step001_test.py
pytest Step2_use_search_tool/giga_step002_test.py
```

### Добавление нового шага
1. Создайте новую директорию в корне проекта
2. Скопируйте структуру из существующих шагов
3. Добавьте тесты
4. Обновите README.md

## Лицензия

MIT
