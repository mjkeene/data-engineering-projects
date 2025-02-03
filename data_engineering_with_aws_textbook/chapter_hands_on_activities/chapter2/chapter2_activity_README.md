<h3>Using the AWS Command Line Interface (CLI) to create Simple Storage Service (S3) buckets</h3>

* To access the CLI on your personal computer, you need to generate a set of access keys (access key ID, which is 
  like a username, and a secret access key, which is like a password). 
* The easiest and most secure way to access the CLI is via the `AWS CloudShell` service, which is accessible via the 
  console. There is no need to generate access keys for your user with this method.


* Use the `aws` command within the console to interact with AWS services.

```shell
aws s3 help
```

<h4>Creating new S3 buckets</h4>

* Each S3 bucket needs to have a globally unique name, and it is recommended that the name be DNS-compliant (i.e., 
  it does not contain periods.) AWS documentation recommends only using periods in an S3 bucket name if you plan on 
  using that bucket to host a static website.
  * Bucket names must be unique across ALL AWS accounts in the global S3 namespace. If any other account has created 
    a bucket, you cannot create a bucket with that name.
  * You can use your account number or initials in the bucket to have a unique bucket name.


<h4>Shell command for creating new bucket</h4>

```shell
aws s3 mb s3://<bucket-name>
```

<h4>Create 3 new buckets which will later be used for data lake data zones</h4>

```shell
aws s3 mb s3://dataeng-landing-zone-mjk25
aws s3 mb s3://dataeng-clean-zone-mjk25
aws s3 mb s3://dataeng-curated-zone-mjk25
```
