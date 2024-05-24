import boto3

# Create a boto3 client for S3
s3_client = boto3.client('s3')

# List buckets
response = s3_client.list_buckets()

# Extract and print bucket names
if 'Buckets' in response:
    print("List of buckets:")
    for bucket in response['Buckets']:
        print(bucket['Name'])
else:
    print("No buckets found.")
