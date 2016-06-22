#!/bin/bzsh
until nc -z postgres 5432; do
    echo "$(date) - waiting for postgres..."
    sleep 1
done
python mysite/manage.py runserver 0.0.0.0:12345
