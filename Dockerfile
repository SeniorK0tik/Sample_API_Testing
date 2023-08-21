FROM python:3.11-buster  AS builder

COPY poetry.lock pyproject.toml ./
RUN python -m pip install --no-cache-dir poetry==1.5.1 \
    && poetry export --without-hashes -f requirements.txt -o requirements.txt

FROM python:3.11-buster

WORKDIR /app

COPY --from=builder requirements.txt ./
RUN python -m pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["python", "-m", "pytest", "-m", "sync_api", "-n", "auto", "--alluredir=./allure-results"]

