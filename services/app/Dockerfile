ARG PYTHON_VERSION=3.8.1-slim-buster
FROM python:${PYTHON_VERSION}

LABEL maintainer="nickname <nickname@info.org>"

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update && apt-get install -y netcat cron vim

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/app/

ENV TZ Asia/Ho_Chi_Minh

# run entrypoint.sh
#ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
