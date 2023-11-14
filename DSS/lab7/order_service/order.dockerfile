FROM python:3.8-slim
WORKDIR /app
COPY order_service.py .
CMD ["python", "order_service.py"]
