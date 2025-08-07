FROM mcr.microsoft.com/playwright/python:v1.44.0-jammy

WORKDIR /var/task

RUN pip install awslambdaric

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN playwright install

COPY app.py .

ENV AWS_LAMBDA_HANDLER=app.lambda_handler

CMD ["python3", "-m", "awslambdaric", "app.lambda_handler"]
