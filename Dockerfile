FROM python:2.7.15-alpine3.7

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt

CMD ["python", "run.py"]