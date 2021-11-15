import boto3



bucket_name = 'udacity-s3-bucket'
client = boto3.client('s3')

response = client.get_object(
    Bucket=bucket_name,
    Key='hello_boto.txt',

)

body = response.get('Body').read().decode('utf-8')
print(body)
print("done!")
