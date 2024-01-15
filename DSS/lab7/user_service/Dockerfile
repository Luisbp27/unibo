FROM python:3.8-slim
WORKDIR /app
RUN pip install flask
COPY user_service.py .
CMD ["python", "user_service.py"]
