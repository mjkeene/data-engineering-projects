from aws_cdk import (
    CfnOutput,
    Stack,
    Duration,
    aws_lambda as _lambda,
    aws_s3 as s3,
    aws_events as events,
    aws_events_targets as targets
)
from aws_cdk.aws_ecr_assets import Platform
from aws_cdk.aws_lambda import DockerImageFunction, DockerImageCode
from constructs import Construct
import os

class WebScrapeCdkStack(Stack):
    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        # Create an S3 bucket to store scraped data
        bucket = s3.Bucket(self, "ScrapedDataBucket",
            versioned=True)
        
        # Create a Lambda function for web scraping
        scraper_function = DockerImageFunction(
            self, "ScraperFunction",
            code=DockerImageCode.from_image_asset("scraper_docker", platform=Platform.LINUX_AMD64),
            timeout=Duration.minutes(2),
            memory_size=1024,
            environment={
                "BUCKET_NAME": bucket.bucket_name,
                "AWS_LAMBDA_HANDLER": "app.lambda_handler",
                "PLAYWRIGHT_BROWSERS_PATH": "0",  # tell playwright to use local browsers
                "PYPPETEER_SKIP_CHROMIUM_DOWNLOAD": "true",  # if you manage your browser manually
                "PWDEBUG": "0",
                "PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD": "1"
            }
        )

        # Grant the Lambda function permissions to write to the S3 bucket
        bucket.grant_write(scraper_function)

        # OPTIONAL: Scheduled scrape via EventBridge
        rule = events.Rule(
            self, "HourlyScrapeRule",
            schedule=events.Schedule.rate(Duration.hours(1)),
            targets=[
                targets.LambdaFunction(
                    handler=scraper_function,
                    event=events.RuleTargetInput.from_object({
                        "url": "https://www.cars.com"
                    })
                )
            ]
        )
        
        # Stack Outputs
        CfnOutput(self, "BucketName",
            value=bucket.bucket_name,
            description="The name of the S3 bucket where scraped data is stored."
        )

        CfnOutput(self, "LambdaFunctionName",
            value=scraper_function.function_name,
            description="The name of the Lambda function used for web scraping."
        )

        CfnOutput(self, "EventBridgeRuleName",
            value=rule.rule_name,
            description="The name of the EventBridge rule that triggers the Lambda function."
        )

# from aws_cdk import (
#     Stack,
#     aws_lambda as _lambda
# )
# from constructs import Construct
# import os

# class WebScrapeCdkStack(Stack):

#     def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
#         super().__init__(scope, construct_id, **kwargs)

#         self.lambda_fn = _lambda.Function(
#             self, "ScraperFunction",
#             runtime=_lambda.Runtime.PYTHON_3_11,
#             handler="handler.lambda_handler",
#             code=_lambda.Code.from_asset("lambda"),
#         )
