release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn devroutes.wsgi --log-file -