FROM python:3.11-slim

WORKDIR /todo

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

RUN mkdir -p /data

CMD ["python", "app.py"]
