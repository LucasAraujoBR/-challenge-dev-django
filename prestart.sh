#! /usr/bin/env sh

python manage.py collectstatic --noinput
python manage.py migrate
python create_superuser.py

# Verifique se o diretório 'static' existe
if [ ! -d "./static" ]; then
  mkdir ./static
fi

python manage.py runserver 0.0.0.0:8000 