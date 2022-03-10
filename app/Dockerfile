FROM python:3.8.5-alpine

EXPOSE 5000

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN apk add gcc musl-dev python3-dev libffi-dev openssl-dev

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
