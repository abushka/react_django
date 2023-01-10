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

python ./backend/manage.py flush --noinput;
python ./backend/manage.py makemigrations;
python ./backend/manage.py migrate;
python ./backend/manage.py runserver 0.0.0.0:8000;

exec "$@"
