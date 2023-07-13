# Dockerfile
FROM python:3.8

ARG DATABASE_URL_ARG
ENV DATABASE_URL=$DATABASE_URL_ARG


RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip install -r requeriments.txt

EXPOSE 5000
CMD ["python", "/app/app.py"]