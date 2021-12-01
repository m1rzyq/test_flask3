FROM python:3.9.7-alpine3.13
COPY . /templates
WORKDIR /templates
RUN pip install -r requirements.txt