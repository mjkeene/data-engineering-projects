import json
import os
import boto3
from urllib.parse import urlparse
from datetime import datetime, timezone
import asyncio
from playwright.async_api import async_playwright
import requests

# Helper function to fetch page content using Playwright
async def fetch_page_content(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-setuid-sandbox"]
        )
        context = await browser.new_context(
            user_agent=(
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/115.0.0.0 Safari/537.36"
            )
        )
        page = await context.new_page()
        await page.goto(url, timeout=20000)  # 20 second timeout
        content = await page.content()
        await browser.close()
        return content
    
def run_async(coro):
    try:
        # If there's an event loop already running (e.g. in Jupyter), use it
        loop = asyncio.get_running_loop()
    except RuntimeError:
        # Otherwise, start a new loop
        return asyncio.run(coro)
    else:
        # If we're already in a loop, create a new task and wait for it
        return loop.run_until_complete(coro)
    
def lambda_handler(event, context):
    url = event.get("url")
    if not url:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing 'url' parameter in the event"})
        }
    
    try:
        response = requests.get(url)
        html_content = response.text.encode('utf-8')
        # html_content = asyncio.run(fetch_page_content(url))
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": f"Failed to fetch page content: {e}"})
        }
    
    # Parse domain and create a filename
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.replace(".", "") # e.g., "example.com" becomes "examplecom"

    # Format date
    date_str = datetime.now(timezone.utc).strftime('%Y-%m-%d')

    # Compose S3 key
    key_prefix = f"{date_str}-{domain}-data-scrape"
    s3_key = f"{key_prefix}/index.html"

    # Upload to S3
    s3 = boto3.client("s3")
    bucket_name = os.environ["BUCKET_NAME"]
    
    try:
        s3.put_object(
            Bucket=bucket_name,
            Key=s3_key,
            Body=html_content,
            ContentType='text/html'
        )
    except Exception as e:
        return {"statusCode": 500, "body": f"Failed to upload to S3: {e}"}
        
    return {
        "statusCode": 200,
        "body": f"Data saved to s3://{bucket_name}/{s3_key}"
    }
