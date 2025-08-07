#!/usr/bin/env python3
import aws_cdk as cdk
from web_scrape_cdk.web_scrape_cdk_stack import WebScrapeCdkStack

app = cdk.App()
WebScrapeCdkStack(app, "WebScrapeCdkStack")

app.synth()
