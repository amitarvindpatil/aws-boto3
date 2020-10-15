import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket():
    # Create bucket
    try:
        s3_client = boto3.client('s3', region_name='us-east-1')
        # location = {'LocationConstraint': region}
        s3_client.create_bucket(Bucket='amitpatil0404')
    except ClientError as e:
        logging.error(e)


def list_buckets():

    s3_client = boto3.client('s3', region_name='us-east-1')
    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')


def upload_file():
    # If S3 object_name was not specified, use file_name
    # Upload the file
    s3_client = boto3.client('s3', region_name='us-east-1')
    try:
        response = s3_client.upload_file('G:/aws-sample/amit.txt', 'amitpatil0404', 'amit_test1.txt', ExtraArgs={
                                         'Metadata': {'name': 'test'}, 'ACL': 'public-read'})
    except ClientError as e:
        logging.error(e)


def download_file():
    s3_client = boto3.client('s3', region_name='us-east-1')

    s3_client.download_file('amitpatil0404', 'amit_test.txt', 'patil.txt')


# create_bucket()
# list_buckets()
upload_file()
# download_file()
