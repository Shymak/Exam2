FROM python:3.9-alpine

WORKDIR /app

COPY Sum.py ./

CMD ["python", "Sum.py"]