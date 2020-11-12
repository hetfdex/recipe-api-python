FROM python:3.9-alpine

LABEL maintainer="hetfdex@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app
ADD . /app

RUN adduser -D hetfdex

USER hetfdex