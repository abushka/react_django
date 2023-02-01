#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
    echo $(ls)
fi

python manage.py flush --noinput;
python manage.py makemigrations;
python manage.py migrate;
python manage.py runserver 0.0.0.0:8000;

exec "$@"
