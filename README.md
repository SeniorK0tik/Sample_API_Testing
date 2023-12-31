# Пример тестирования API

Проект является примером построения API тестов.

**Установка**
- Необходим Python >= 3.10
```
git clone https://github.com/SeniorK0tik/Sample_API_Testing
pip install poetry
poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi
```
- Измени название `.env-dist` на `.env`

**Запуск тестов**

**Sync вариант(рекомендуется)**
```
python -m pytest -m sync_api -n auto --alluredir=./allure-results
```
**Async вариант**
```
python -m pytest -m async_api -n auto --alluredir=./allure-results
```

**Запуск allure**
- Необходимо установить allure локально
```
allure serve
or
allure generate
```

Комментарий:
- Async вариант был добавлен в качестве эксперимента и является не очень хорошей идеей для реалиазации его в автотестах по многим причинам... Так что пользуйся sync вариантом.
- Для реализации проверки можно также использовать Pycamel. Но реализованый кастомный вариант тоже выполняет необходимый функционал.
