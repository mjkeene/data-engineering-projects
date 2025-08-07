# Web Scrape CDK

A serverless web scraping application built with AWS CDK (Python). This project provisions:

* An AWS Lambda function that scrapes data from a given URL.
* An S3 bucket to store the scraped HTML content.
* IAM permissions to allow Lambda to write to the S3 bucket.
* (Optional) An EventBridge rule to schedule scraping tasks.

## 📁 Project Structure

```
web-scrape-cdk/
├── app.py
├── cdk.json
├── requirements.txt 
├── README.md
├── web_scrape_cdk/
│ └── web_scrape_cdk_stack.py
├── lambda/
│ └── scraper.py
```

## 🚀 Deploying the Stack

1. **Set up a virtual environment:** (recommended):

```bash
python -m venv .env
source .env/bin/activate
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Bootstrap your AWS environment (only needed once per environment):**

```bash
cdk bootstrap
```

4. **Deploy the stack:**

```bash
cdk deploy
```

## Invoking the Lambda Function

You can test the Lambda function via the AWS Console or programmatically using the AWS CLI or SDK. Example payload:

```json
{
  "url": "https://example.com"
}
```

This will fetch the HTML from the provided URL and save it to your S3 bucket under a key like:

```bash
scraped/example.com.html
```

## Cleanup 
To remove all resources created by this stack:

```bash
cdk destroy
```

## Notes
* This is a basic scraper and may not work well on JavaScript-heavy pages.
* For advanced scraping, consider using tools like Playwright, Puppeteer, or headless Chrome with Lambda containers.

