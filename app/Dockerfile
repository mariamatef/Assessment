FROM python:3.8.5-alpine

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev libmysqlclient-dev python-dev

RUN pip install -r requirements.txt

CMD ["python","app.py"]
