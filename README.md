# fuzzy-lamp
A Flask Hello World example

## Prerequisites

This application installs and runs with [poetry](https://python-poetry.org/).
If you don't have it, please follow [Installation Guide](https://python-poetry.org/docs/#installation).
You also can install it running the following command: `python3 -m pip install poetry --user`

## Install

```bash
poetry install
```

## Run

Copy environment variables from `env.dist`. 

```bash
cp env.dist .env
```
(If you came from v0.0.1 do it again to update Environment Variables)

The run the Flask Development server using `poetry`

```bash
poetry run flask run --host=0.0.0.0
```

### Docker

Build docker image.

```bash
docker build . -t fuzzy-lamp:0.0.2
```

Run the app using `docker` instead of `poetry`.

```bash
docker run --rm --name fuzzy-lamp-1 -v $PWD:/usr/src/app -p 5000:5000 fuzzy-lamp:0.0.2
```