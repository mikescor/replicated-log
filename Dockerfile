FROM python:3.10-buster

ARG POETRY_VERSION=1.2.2

ENV PYTHONUNBUFFERED 1

RUN mkdir /service

COPY protos/ /service/protos/
COPY src/ service/src/

WORKDIR /service/src

COPY pyproject.toml .
COPY poetry.lock .
COPY .git .git

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false && poetry install --no-cache --no-root
RUN python -m grpc_tools.protoc -I ../protos --python_out=. --grpc_python_out=. ../protos/log.proto

CMD ["python", "server.py"]
EXPOSE 50051