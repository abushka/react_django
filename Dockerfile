# Pull base image
FROM python:3.9.6-alpine

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache bash

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy run_django.sh
COPY ./run_django.sh .

RUN chmod +x ./run_django.sh

# copy project
# test
COPY . /code/

# run run_django.sh
ENTRYPOINT [ "sh", "./run_django.sh" ]

