FROM python:3.6.5-alpine3.7

RUN apk add --no-cache --update git make gcc python3-dev musl-dev && \
    set -ex && \
    pip install --no-cache-dir pipenv==10.1.2

WORKDIR /app
ADD . .

RUN set -ex && \
    pipenv install --dev --system --deploy