import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Name of the table to query
table_name = 'Studenttable'

# Define the key condition expression and expression attribute values
key_condition_expression = "#roll = :roll_val AND #name = :name_val"
expression_attribute_values = {":roll_val": {'N': '227'}, ":name_val": {'S': 'Jagruti'}}
expression_attribute_names = {"#roll": "Roll NO", "#name": "Name"}  

# Perform the query operation
response = dynamodb_client.query(
    TableName=table_name,
    KeyConditionExpression=key_condition_expression,
    ExpressionAttributeValues=expression_attribute_values,
    ExpressionAttributeNames=expression_attribute_names
)

# Retrieve the items from the response
items = response['Items']

# Print the items
for item in items:
    print(item)
