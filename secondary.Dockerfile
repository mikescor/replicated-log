FROM python:3.10.6-slim-buster as builder

ARG POETRY_VERSION=1.2.2

RUN python -m pip install --upgrade pip
RUN python -m pip install poetry==${POETRY_VERSION}
RUN poetry config virtualenvs.create false
RUN mkdir /service

COPY protos/msg_replication.proto /service/protos/
COPY pyproject.toml poetry.lock ./

RUN python -m venv /opt \
    && . /opt/bin/activate \
    && poetry install --no-root

FROM python:3.10.6-slim-buster as final

ENV PYTHONUNBUFFERED=1 \
    PATH=/opt/bin:$PATH \
    PYTHONPATH=/opt/lib/python3.10/site-packages:$PYTHONPATH

COPY --from=builder /opt /opt

WORKDIR /service/src

COPY src/msg_replication_pb2.py .
COPY src/msg_replication_pb2_grpc.py .
COPY src/secondary.py .
COPY src/logging.yaml .

EXPOSE 50051
CMD ["python", "secondary.py"]
