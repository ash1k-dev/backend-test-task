FROM python:3.10.11-slim-buster
WORKDIR /app
COPY ./requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir
COPY . .
CMD ["uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "8000"]
