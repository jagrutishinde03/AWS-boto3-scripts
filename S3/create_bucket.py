import boto3

# Create a boto3 client for S3
s3_client = boto3.client('s3')

# Prompt the user to enter the name of the bucket to create
bucket_name = input("Enter the name of the bucket to create: ")

# Create the bucket
try:
    s3_client.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except Exception as e:
    print(f"An error occurred while creating the bucket: {e}")
