FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /var/task

ARG CACHEBUST=1

RUN pip install awslambdaric

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY app.py .

ENV AWS_LAMBDA_HANDLER=app.lambda_handler

CMD ["python3", "-m", "awslambdaric", "app.lambda_handler"]
