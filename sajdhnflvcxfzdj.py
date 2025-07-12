import boto3
from botocore.exceptions import ClientError
from boto3.session import Session

S3_CLIENT = boto3.client("s3", region_name="us-east-2")

def create_bucket(bucket_name: str) -> {}:
    """
    This function creates a bucket using the provided name.

    This bucket utilizes the boto3 library to create a bucket in
    a provided AWS account when executed. The response contains
    basic details describing the newly created bucket. It throws
    a ClientError should something fail in AWS.

    :param bucket_name:
    :type str:
    :return: dict:
    """
    try:
        session = Session("s3", "us-east-2")
        s3_client = session.client("s3", region_name="us-east-2")
        response = s3_client.create_bucket(Bucket=bucket_name)
        return response
    except ClientError as e:
        print(e)

if __name__ == "__main__":
    bucket_name = "<insert bucket name>"
    create_bucket(bucket_name=bucket_name)
