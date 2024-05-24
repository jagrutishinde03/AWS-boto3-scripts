import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Define the table schema
table_name = 'Studenttable'
attribute_definitions = [
    {
        'AttributeName': 'Roll NO',
        'AttributeType': 'N'  # Number data type
    },
    {
        'AttributeName': 'Name',
        'AttributeType': 'S'  # String data type
    },

]

# Define the key schema
key_schema = [
    {
        'AttributeName': 'Roll NO',
        'KeyType': 'HASH'  # Partition key
    },
    {
        'AttributeName': 'Name',  
        'KeyType': 'RANGE'  # Sort key
    }
]

# Define provisioned throughput
provisioned_throughput = {
    'ReadCapacityUnits': 5,
    'WriteCapacityUnits': 5
}

# Create the table
try:
    response = dynamodb_client.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput=provisioned_throughput
    )
    print(f"Table '{table_name}' created successfully.")
except Exception as e:
    print(f"An error occurred while creating table '{table_name}': {e}")
