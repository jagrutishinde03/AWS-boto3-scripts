import boto3

# Create a boto3 client for S3
s3_client = boto3.client('s3')

# Prompt the user to enter the name of the bucket
bucket_name = input("Enter the name of the bucket: ")

# Prompt the user to enter the local file path to upload
file_paths = input("Enter the local file paths to upload (separated by spaces): ").split()

# Upload files to the bucket
for file_path in file_paths:
    # Extract the file name from the file path
    file_name = file_path.split('/')[-1]
    
    # Upload the file to the bucket
    try:
        s3_client.upload_file(file_path, bucket_name, file_name)
        print(f"File '{file_name}' uploaded successfully to bucket '{bucket_name}'.")
    except Exception as e:
        print(f"An error occurred while uploading file '{file_name}': {e}")
