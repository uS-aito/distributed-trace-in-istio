FROM python:3.6.10-slim-buster

WORKDIR /root

COPY ./src/service2.py service2.py
RUN ["pip", "install", "flask", "requests"]

CMD ["python", "service2.py", "8081"]