import boto3
import awswrangler as wr
import urllib.parse as unquote_plus


def lambda_handler(event, context):
    # Get the source bucket and object name as passed to the Lambda function
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = unquote_plus.unquote_plus(record['s3']['object']['key'])
        print(f'Key: {key}')

    # Set the DB and table name based on the last 2 elements of the path prior to filename
    key_list = key.split('/')
    print(f'key_list: {key_list}')
    db_name = key_list[-3]
    table_name = key_list[-2]

    # Debugging information, output path
    print(f'Bucket: {bucket}')
    print(f'Key: {key}')
    print(f'DB Name: {db_name}')
    print(f'Table Name: {table_name}')

    input_path = f's3://{bucket}/{key}'
    print(f'Input Path: {input_path}')
    output_path = f's3://dataeng-clean-zone-mjk25/{db_name}/{table_name}'
    print(f'Output Path: {output_path}')

    # Read the CSV file from S3
    input_df = wr.s3.read_csv(input_path)

    # Read glue databases, create if necessary
    current_databases = wr.catalog.databases()
    if db_name not in current_databases['Database'].values:
        wr.catalog.create_database(db_name)
        print(f'Database {db_name} did not exist ... creating.')
    else:
        print(f'Database {db_name} already exists.')

    # Use Pandas SDK to create a Parquet file containing data read from CSV file
    result = wr.s3.to_parquet(
        df=input_df,
        path=output_path,
        dataset=True,
        database=db_name,
        table=table_name,
        mode='append'
    )

    print('RESULT: ')
    print(result)
    return result
