FROM python:3.7

RUN apt-get install default-libmysqlclient-dev gcc  -y

RUN pip3 install mysqlclient
RUN pip install django
WORKDIR /app/

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]

EXPOSE 8000