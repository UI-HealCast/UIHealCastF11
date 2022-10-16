release: sh -c 'python manage.py migrate && python manage.py makemigrations'
web: gunicorn project_django.wsgi --log-file -