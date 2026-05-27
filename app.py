import boto3
from botocore.exceptions import ClientError

# Create S3 client
s3 = boto3.client('rds')

def list_buckets():
    try:
        response = s3.list_buckets()

        print("Available S3 Buckets:")
        for bucket in response['Buckets']:
            print(f" - {bucket['dev']}")

    except ClientError as e:
        print(f"Error: {e}")

def upload_file(file_name, bucket_name, object_name=None):
    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print(f"File '{file_name}' uploaded to bucket '{bucket_name}'")

    except ClientError as e:
        print(f"Upload failed: {e}")

# Run functions
list_buckets()

# Example upload
upload_file(
    file_name='sample.txt',
    bucket_name='my-devops-bucket'
)
