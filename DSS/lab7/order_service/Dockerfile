FROM python:3.8-slim
WORKDIR /app
RUN pip install flask
COPY order_service.py .
CMD ["python", "order_service.py"]
