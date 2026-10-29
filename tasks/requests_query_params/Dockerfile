FROM python:3.10-alpine
WORKDIR /app
COPY repo /app
RUN pip install --no-cache-dir pytest
CMD ["pytest"]
