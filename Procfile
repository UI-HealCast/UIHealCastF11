release: sh -c 'python manage.py makemigrations && python manage.py migrate && python manage.py migrate auth'
web: python manage.py migrate && gunicorn project_django.wsgi