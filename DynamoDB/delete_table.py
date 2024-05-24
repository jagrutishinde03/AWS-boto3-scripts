import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Ask the user for the name of the table to delete
table_name = input("Enter the name of the table you want to delete: ")

# Delete the table
response = dynamodb_client.delete_table(
    TableName=table_name
)

print(f"Table '{table_name}' deleted successfully.")
