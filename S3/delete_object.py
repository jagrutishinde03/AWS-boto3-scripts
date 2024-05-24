import boto3

# Create a boto3 client for S3
s3_client = boto3.client('s3')

# Prompt the user to enter the name of the bucket
bucket_name = input("Enter the name of the bucket: ")

# Prompt the user to enter the key of the object to delete
object_key = input("Enter the key of the object to delete: ")

# Delete the object from the bucket
try:
    response = s3_client.delete_object(
        Bucket=bucket_name,
        Key=object_key
    )
    print(f"Object '{object_key}' deleted successfully from bucket '{bucket_name}'.")
except Exception as e:
    print(f"An error occurred while deleting object '{object_key}' from bucket '{bucket_name}': {e}")
