FROM python:3.9-alpine

LABEL maintainer="hetfdex@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt .

RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps gcc libc-dev linux-headers postgresql-dev

RUN pip install -r requirements.txt

RUN apk del .tmp-build-deps

WORKDIR /app
ADD . /app

RUN adduser -D hetfdex

USER hetfdex