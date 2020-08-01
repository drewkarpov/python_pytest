FROM python:3.8

RUN mkdir -p /opt/app
WORKDIR /opt/app


RUN pip install --upgrade pip
RUN python -m venv pytest-venv

COPY . /opt/app

RUN pip install -r requirements.txt

ENV PYTHONPATH /opt/app/

CMD ["./manage.py", "runserver"]