FROM python:3.7-slim

RUN mkdir /code
WORKDIR /code
COPY . /code/

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

RUN python manage.py makemigrations
RUN python manage.py migrate
