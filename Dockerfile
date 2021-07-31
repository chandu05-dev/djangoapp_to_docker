FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD="iodex123"
ENV DJANGO_SUPERUSER_USERNAME="iodex_admin"
ENV DJANGO_SUPERUSER_EMAIL="iodex@ex.com"
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/



ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
