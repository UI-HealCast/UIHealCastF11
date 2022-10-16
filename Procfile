release: sh -c 'python manage.py migrate && python manage.py makemigrations && python manage.py migrate auth'
web: gunicorn project_django.wsgi --log-file -