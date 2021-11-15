from logging import exception
import boto3



bucket_name = 'udacity-s3-bucket'
file_name = 'index.html'

client = boto3.client('s3')

try:
    file = open(file_name, 'br')
    response = client.put_object(
        Body=file,
        Bucket=bucket_name,
        Key='hello_boto.txt',
        ServerSideEncryption='aws:kms',
        SSEKMSKeyId='db920116-96ca-463e-9176-96f900049fbc'
    )
    print(response)
except:
    print("Something went wrong!")

finally:
    print("done!")
