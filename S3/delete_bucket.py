import boto3

# Create a boto3 client for S3
s3_client = boto3.client('s3')

# Prompt the user to enter the name of the bucket to delete
bucket_name = input("Enter the name of the bucket to delete: ")

try:
    # Delete the bucket
    s3_client.delete_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' deleted successfully.")
except Exception as e:
    print(f"An error occurred while deleting bucket '{bucket_name}': {e}")
