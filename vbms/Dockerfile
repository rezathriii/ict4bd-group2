FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

RUN chmod +x /app/wait-for-idf2fmu.sh

CMD ["sh", "-c", "exec /app/wait-for-idf2fmu.sh"]
