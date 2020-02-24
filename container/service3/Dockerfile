FROM python:3.6.10-slim-buster

WORKDIR /root

COPY ./src/service3.py service3.py
RUN ["pip", "install", "flask", "requests"]

CMD ["python", "service3.py", "8082"]