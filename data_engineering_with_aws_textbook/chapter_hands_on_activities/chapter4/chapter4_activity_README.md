<h2>Configuring Lake Formation Permissions</h2>

<h3>Create a new IAM User</h3>

* This user will be our data lake user.
* They will have permission to:
  * access a specific database and table in the Glue catalog
  * access specific S3 locations that contain the underlying files associated with our Glue table objects
  * use the Athena service to run SQL queries against the data lake

* Pull up the `AmazonAthenaFullAccess` policy JSON, and copy it.
* Under the Glue permissions, specify the following resources:

```json
"arn:aws:glue:*:*:catalog",
"arn:aws:glue:*:*:database/cleanzonedb",
"arn:aws:glue:*:*:database/cleanzonedb*",
"arn:aws:glue:*:*:table/cleanzonedb/*"
```

* Under the S3 permissions, specify the following resources:

```json
"arn:aws:s3:::aws-athena-query-results-*",
"arn:aws:s3:::dataeng-clean-zone-mjk25/*"
```

* Save the policy with the name `AthenaAccessCleanZoneDB`.

* Now we will create a data lake user.
* Create a new IAM user named `datalake-user`.
* Attach the `AthenaAccessCleanZoneDB` just created.
* Create an S3 bucket that can store Athena query results called `aws-athena-query-results-dataengbook-mjk25`


* You can now run the query from the `datalake-user`. Sign out and sign back in as that user.
* Navigate to Athena, and set the `aws-athena-query-results-dataengbook-mjk25` S3 bucket as query result location.
* Run the following SQL query:

```sql
SELECT *
FROM cleanzonedb.csvtoparquet
```

<h3>Transitioning to managing fine-grained permissions with AWS Lake Formation</h3>

* Here we will modify `cleanzonedb` and the tables in that database to make use of the Lake Formation permissions model.
* Lake Formation adds a layer of permissions that work in addition to the IAM policy permissions.
* By default, every database table in the catalog has a special permission enabled that effectively tells Lake 
  Formation to just use IAM permissions and to ignore any permissions that may have been granted in Lake Formation.
  * This is called <b>Pass-Through</b> permission, as it allows security checks to be validated at the IAM level, 
    but then passes through Lake Formation without doing any additional permission checks.


* In Lake Formation, click on databases, and then actions, and then view permissions.
* There are two permissions for `cleanzonedb`:
  * `DataEngLambdaS3CWGlueRole` which was assigned to the Lambda function that created the database
  * `IAMAllowedPrincipals` which is the pass-through permission mentioned previously, which effectively means that 
    permissions at the Lake Formation layer are ignored. If this special permission was not assigned, only 
    `DataEngLambdaS3CWGlueRole` would be able to access the database.
    * However, since it has been assigned, any user who has been granted permissions to this database through an IAM 
      policy, such as `datalake-user`, will be able to successfully access the database.
* To enable Lake Formation permissions on this database, we can remove the `IAMAllowedPrincipals` permission from 
  the database.
* Revoke the permissions, then do the same for the `csvtoparquet` table in the database.

<h3>Granting Lake Formation Permissions</h3>

* By removing the `IAMAllowedPrincipals` permission from the `cleanzonedb` database and the `csvtoparquet` table, we 
  have effectively enabled Lake Formation permissions on those resources.
  * Now, if any principal needs to access that database or table, they need both IAM permissions, as well as Lake 
    Formation permissions.
* If we had enabled Lake Formation permissions on all databases and tables, then we could modify our user's IAM 
  policy permissions to give them access to all data catalog objects. This is because we know that they would only 
  be able to access those databases and tables where they had been granted specific Lake Formation permissions.
* If all databases and tables had the `IAMAllowedPrincipals` permissions removed and specific permissions granted to 
  users instead, we could apply the `AmazonAthenaFullAccess` (i.e., not restrict access to a specific database / 
  table in Lake Formation).
* When using Lake Formation permissions, you do not need to specifically grant access to the underlying S3 files. 
  Compatible analytic tools (like Athena) are granted access to the underlying S3 data using temporary credentials 
  provided by Lake Formation.
  * If using Lake Formation permissions, we can remove permissions to the underlying S3 data from the user's IAM 
    policy.
* We can limit access within a table to specific columns for a user by excluding access to those columns. Here we 
  will exclude the `favorite_num` column for `datalake-user`.
* Enabling column-level permissions is not something that would be possible if we were just using IAM-level 
  permissions, as that is a Lake Formation-specific feature.
