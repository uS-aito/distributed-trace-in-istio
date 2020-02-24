FROM python:3.6.10-slim-buster

WORKDIR /root

COPY ./src/service1.py service1.py
RUN ["pip", "install", "flask", "requests"]

CMD ["python", "service1.py", "8080"]