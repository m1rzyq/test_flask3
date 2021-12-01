FROM python:3.9.7-alpine3.13
COPY . /python_flask
WORKDIR /python_flask
RUN pip install -r requirements.txt