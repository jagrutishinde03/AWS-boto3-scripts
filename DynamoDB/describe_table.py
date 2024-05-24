import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Prompt the user to enter the name of the table
table_name = input("Enter the name of the table: ")

# Describe the table
try:
    response = dynamodb_client.describe_table(TableName=table_name)
    table_description = response['Table']
    print("Table Description:")
    print("Table Name:", table_description['TableName'])
    print("Attribute Definitions:", table_description['AttributeDefinitions'])
    print("Key Schema:", table_description['KeySchema'])
    print("Provisioned Throughput:", table_description['ProvisionedThroughput'])
    # Add more details as needed
except dynamodb_client.exceptions.ResourceNotFoundException:
    print(f"The table '{table_name}' does not exist.")
except Exception as e:
    print(f"An error occurred while describing table '{table_name}': {e}")
