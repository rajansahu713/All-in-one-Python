
import boto3
ACCESS_KEY_ID = "AWS_S3_ACCESS_KEY"
SECRET_ACCESS_KEY = "AWS_S3_SECRET_KEY"
PATH_IN_COMPUTER = 'Data/original.csv'
BUCKET_NAME = "bucket name"
KEY = 'original.csv' # file path in S3

s3_resource = boto3.resource('s3',
    aws_access_key_id = ACCESS_KEY_ID,
    aws_secret_access_key = SECRET_ACCESS_KEY
)

s3_resource.Bucket(BUCKET_NAME).put_object(
    Key = KEY,
    Body = open(PATH_IN_COMPUTER, 'rb')
)