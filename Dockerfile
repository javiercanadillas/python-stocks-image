from python:latest

WORKDIR /app

COPY . /app

CMD ["python", "stocks.py"]
