import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Name of the table to scan
table_name = 'Studenttable'

# Define the filter expression and expression attribute values
filter_expression = "#cgpa >= :cgpa"
expression_attribute_values = {":cgpa": {'N': '9.0'}}  # CGPA greater than or equal to 9.0
expression_attribute_names = {"#cgpa": "Cgpa"}  # Cgpa is a reserved keyword, so using expression attribute names to avoid conflict

# Perform the scan operation with the filter
response = dynamodb_client.scan(
    TableName=table_name,
    FilterExpression=filter_expression,
    ExpressionAttributeValues=expression_attribute_values,
    ExpressionAttributeNames=expression_attribute_names
)

# Retrieve the items from the response
items = response['Items']

# Print the items
for item in items:
    print(item)
