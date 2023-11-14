FROM python:3.8-slim
WORKDIR /app
COPY user_service.py .
CMD ["python", "user_service.py"]
