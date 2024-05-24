import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Name of the table to update the item in
table_name = 'Studenttable'

# Define the key of the item you want to update
key = {
    'Roll NO': {'N': '227'},  # Number attribute
    'Name': {'S': 'Jagruti'}  # String attribute
}

# Define the update expression and attribute values
update_expression = "SET Cgpa = :val"
expression_attribute_values = {":val": {'N': '9.11'}}  # New CGPA value

# Update the item
response = dynamodb_client.update_item(
    TableName=table_name,
    Key=key,
    UpdateExpression=update_expression,
    ExpressionAttributeValues=expression_attribute_values
)
print("Item updated successfully.")


'''

table_name = 'Student'

response = client.update_item(
    TableName=table_name,
    Key={
        'RollNo': {
            'N': str(9)
        }
    },
    UpdateExpression='SET Cgpa = :Cgpa',
    ExpressionAttributeValues={':Cgpa': {'N': '8.4'}},
    ReturnValues='ALL_NEW'
)

print("Updated Item:", response.get('Attributes', {}))'''