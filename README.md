# flask-app

This is a example flask app that can be used as a template repository for new flask apps.

The application relies on the app folder, being the `main.py` its entrypoint.

It aims to use the latest version of Python, Flask and Gunicorn. Feel free to make a pull request if it's not.

# Running the app

## Docker

[Docker](https://www.docker.com/) and [Docker Compose](https://www.docker.com/) make things easy!

```sh
docker-compose up
# or if you want to run detached
docker-compose up -d
```

## Natively

There is a comprehensive `Makefile` in the project that can be used.

```sh
# install dependencies
make
# runs the app
make run
```
