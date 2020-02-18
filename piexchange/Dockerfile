FROM python:latest
ENV LANG C.UTF-8

RUN mkdir /piexchange

RUN apt-get -y update
RUN apt-get install -y python python-pip python-dev python-psycopg2 postgresql-client vim net-tools

ADD run_command.sh /piexchange/requirements.txt

ADD requirements.txt /piexchange/requirements.txt
RUN pip install -r /piexchange/requirements.txt

RUN apt-get -y update && apt-get -y autoremove
WORKDIR /piexchange

EXPOSE 8000

CMD gunicorn -b :8000 piexchange.wsgi

CMD [ "python", "manage.py makemigrations search" ]

CMD [ "python", "manage.py migrate" ]

CMD [ "python", "manage.py runserver 0.0.0.0:8000" ]