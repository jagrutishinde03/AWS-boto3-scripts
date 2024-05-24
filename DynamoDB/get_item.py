import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Perform the get_item operation
try:
    response = dynamodb_client.get_item(
        TableName='Studenttable',
        Key={
            'Roll NO': {'N': '227'},  # Specify the hash key
            'Name': {'S': 'Jagruti'}   # Specify the sort key
        }
    )
    item = response.get('Item')
    if item:
        print("Item found:", item)
    else:
        print("Item not found.")
except Exception as e:
    print(f"An error occurred while getting item from table: {e}")
