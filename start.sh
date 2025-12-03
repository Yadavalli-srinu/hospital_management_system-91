python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn hospital_project.wsgi:application --bind 0.0.0.0:$PORT