FROM python:3.9-slim

LABEL maintainer="giemzadariusz@gmail.com"\
    description="Simple REST API to retrieve medical data"

RUN mkdir /code

COPY ./ /code/

RUN pip3.9 install -r /code/requirements.txt

WORKDIR /code/

RUN --mount=type=secret,id=_env,dst=/etc/secrets/.env cat /etc/secrets/.env

ENV SNOWFLAKE_PASS=${SNOWFLAKE_PASS}
ENV SNOWFLAKE_USER=${SNOWFLAKE_USER}
ENV SNOWFLAKE_ACCOUNT=${SNOWFLAKE_ACCOUNT}

EXPOSE 8000

CMD uvicorn main:app --app-dir src/ --host 0.0.0.0 --port 8000 --reload