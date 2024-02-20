FROM python:3.11-slim-bullseye AS builder

ADD poetry.lock /src/app-root/
ADD pyproject.toml /src/app-root/

RUN pip install poetry

RUN pwd

WORKDIR /src/app-root
RUN poetry export -o requirements.txt \
    && poetry export --dev -o requirements_dev.txt

FROM python:3.11-slim-bullseye AS runner

COPY --from=builder /src/app-root/requirements.txt /src/app-root/requirements.txt

RUN apt-get update && apt upgrade -y
RUN apt-get install -y --no-install-recommends curl build-essential gcc make && apt-get clean && apt-get autoremove
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

WORKDIR /src/app-root
RUN pip install -r requirements.txt

ADD meteoch /src/app-root/meteoch


CMD ["uvicorn", "--host", "0.0.0.0", "--timeout-keep-alive", "30", "--port", "8080", "meteoch.asgi:app"]
