#!/bin/bash

#gunicorn --log-level info --log-file=/gunicorn.log --workers 4 --name app -b 0.0.0.0:8000 --reload app.app:app

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py create_db

exec "$@"