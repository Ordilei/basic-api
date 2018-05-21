FROM python:2.7.15-alpine3.7

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]