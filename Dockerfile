FROM python:3.9.7-alpine3.13
COPY . /
WORKDIR /
RUN pip install -r requirements.txt