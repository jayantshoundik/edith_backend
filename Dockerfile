FROM python:latest

WORKDIR /src
COPY . .
EXPOSE 8002

RUN pip install virtualenv
RUN virtualenv virtual
RUN /bin/bash -c "source virtual/bin/activate"
RUN pip install -r requirements.txt
RUN python manage.py makemigrations adminpanel userpanel commonpanel
RUN python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8002" ]
