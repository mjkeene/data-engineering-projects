<h2>Triggering an AWS Lambda function when a new file arrives in an S3 Bucket</h2>

* Lambda function should automatically be triggered when a .csv file is uploaded to the landing zone bucket. Lambda 
  function will convert the file to parquet and then write it to the target bucket (clean zone S3 bucket).

<h3>Creating a Lambda layer containing the AWS SDK for pandas library</h3>

* Navigate to https://github.com/aws/aws-sdk-pandas/releases
* Download the `awswrangler-layer-3.11.0-py3.10.zip`
* Log in to AWS Console as Admin user
* Double check region is as desired
* Go to Lambda Layer -> name it something like `awsSDKpandas311_python310` -> attach zip file

<h3>Creating IAM policy and role for the Lambda function</h3>

* We'll be using the three S3 buckets from last chapter (landing zone, clean zone, curated zone)
* Lambda function needs the following permissions:


1. Read our source S3 bucket (for example, dataeng-landing-zone-<initials>).
2. Write to our target S3 bucket (for example, dataeng-clean-zone-<initials>).
3. Write logs to Amazon CloudWatch.
4. Access to all Glue API actions (to enable the creation of new databases and tables).


* The first step to creating the new AWS IAM role with these permissions is to create a new policy. The policy is in 
  the `iam_policy.json` file in this same directory.
* Note that the S3 buckets are listed twice -- once with no slash, and once with `/*` at the end. You must 
  explicitly give permission to access the bucket, AND the objects within that bucket.
* In a production environment, the Glue permissions should be limited in scope.
* Next, create a <b>Role</b> by selecting Lambda as our trusted entity AWS service.
* In the "attach permissions" section, select the policy we just created. Provide a name like 
  `DataEngLambdaS3CWGlueRole` and create.

<h3>Creating the Lambda function</h3>

* Click on Create function, author from scratch, python 3.10 runtime, and change the default execution role to the 
  role we just created.
* Add the custom Lambda layer with the AWS SDK for pandas that we created earlier.
* Finally, update the `lambda_handler` code in the lambda function code section, which can be found in the 
  `lambda_function.py` file in this directory.
* Deploy the code from the lambda function
* Make sure the timeout is increased beyond the default 3 seconds to 1 minute or more
  * I ended up increasing it to 80 seconds, since lambda was actually timing out and retrying, resulting in 2 
    parquet files being written per upload. In reading further about this:
    * S3 event notifications are not guaranteed to be delivered exactly one time; it can be delivered multiple times. 
    * If Lambda fails or times out, it can retry (and it does by default).


* If it's timing out, then the timeout needs to be increased (or make the function more efficient).
* Could add the key to DynamoDB, and check to see if that key has already been processed to ensure it is only 
  processed one time

<h3>Configuring the Lambda function to be triggered by an S3 upload</h3>

* Click on Add trigger in Lambda, S3 service, then select landing zone bucket
* We want all object create events to trigger the function
* Suffix should be .csv to only run with .csv files
* <b>Recursive invocation</b> can happen if you set up a trigger on a specific bucket to run a Lambda function, and 
  then you get your Lambda function to create a new file in the same bucket and path. 
  * Make sure you configure for the LANDING ZONE bucket and not the CLEAN ZONE bucket that the Lambda function will 
    write to.

<h4>Final result</h4>

* The Lambda function was triggered and wrote out a Parquet-formatted file to the target S3 bucket and created a 
  Glue database and table. 
* You can run the following command in CloudShell to ensure that a Parquet file has been written to the target bucket:

`aws s3 ls s3://dataeng-clean-zone-mjk25/cleanzonedb/csvtoparquet/`
