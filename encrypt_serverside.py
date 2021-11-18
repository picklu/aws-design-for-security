import os
import boto3
from dotenv import load_dotenv


load_dotenv()
client = boto3.client('s3')


def encrypt_file(file_name, upload_as):
    """Upload file_name as upload_as"""
    with open(file_name, 'br') as file:
        response = client.put_object(
            Body=file,
            Bucket=os.getenv('BUCKET_NAME'),
            Key=upload_as,
            ServerSideEncryption=os.getenv('ENCRYPTION'),
            SSEKMSKeyId=os.getenv('KEY_ARN')
        )
    return response


if __name__ == "__main__":
    response = encrypt_file('index.html', 'hello_bucket.txt')
    print(response.get('ResponseMetadata', {}).get('HTTPStatusCode', 1))
    print("done!")
