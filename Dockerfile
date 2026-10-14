FROM python:3.14-slim

LABEL maintainer="oleh.kuper.dev@gmail.com"

ENV PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN pipenv install --deploy --system

COPY . .

RUN useradd --no-create-home appuser

USER appuser
