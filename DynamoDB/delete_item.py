import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Name of the table
table_name = 'Studenttable'

# Ask the user for the name of the item to delete
name_to_delete = input("Enter the name of the item you want to delete: ")

# Perform a scan operation to retrieve the item(s) with the specified name
response = dynamodb_client.scan(
    TableName=table_name,
    FilterExpression="#name = :name_val",
    ExpressionAttributeValues={":name_val": {'S': name_to_delete}},
    ExpressionAttributeNames={"#name": "Name"}
)

# Retrieve the items from the response
items = response['Items']

# Delete each item
for item in items:
    key = {
        'Roll NO': item['Roll NO'],  # Roll NO attribute
        'Name': item['Name']         # Name attribute
    }
    dynamodb_client.delete_item(
        TableName=table_name,
        Key=key
    )
    print(f"Item with name '{name_to_delete}' deleted successfully.")
