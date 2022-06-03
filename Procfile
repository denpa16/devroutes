release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn routes.wsgi --log-file -