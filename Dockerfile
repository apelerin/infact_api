FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN --mount=type=secret,id=PG_NAME \
  --mount=type=secret,id=PG_USER \
  --mount=type=secret,id=PG_PASSWORD \
  --mount=type=secret,id=PG_PORT \
   export PG_NAME=$(cat /run/secrets/PG_NAME) && \
   export PG_USER=$(cat /run/secrets/PG_USER) && \
   export PG_PASSWORD=$(cat /run/secrets/PG_PASSWORD) && \
   export PG_PORT=$(cat /run/secrets/PG_PORT) && \
    pip install -r requirements.txt
COPY . /code/
