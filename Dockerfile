FROM python:3.12-bookworm

LABEL authors="Nick Smirnov"
EXPOSE 8001

ENV POSTGRES_USER username
ENV POSTGRES_PASSWORD password
ENV POSTGRES_HOST localhost
ENV POSTGRES_PORT 5432
ENV POSTGRES_DB postgres
ENV SQL_DRIVER postgresql+asyncpg

WORKDIR /src

COPY . .

RUN python -m ensurepip --upgrade && pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8001"]
