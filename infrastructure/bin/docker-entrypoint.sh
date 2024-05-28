#!/usr/bin/env bash

sleep 3
echo "Waiting for postgres..."
echo "Migration started"
django-admin makemigrations
django-admin migrate

echo "Creating superuser"
django-admin createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL

echo "Starting server"
django-admin runserver "0.0.0.0:8000"
