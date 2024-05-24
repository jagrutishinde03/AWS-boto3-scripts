import boto3

# Create a boto3 client for DynamoDB
dynamodb_client = boto3.client('dynamodb')

# Name of the table to put the items into
table_name = 'Studenttable'

# Items to put into the table
items = [
    {
        'Roll NO': {'N': '227'},   # Number attribute
        'Name': {'S': 'Jagruti'},     # String attribute
        'Surname': {'S': 'Shinde'},   # String attribute
        'Cgpa': {'N': '8.75'},     # Number attribute
        'Age': {'N': '21'}         # Number attribute
    },
    {
        'Roll NO': {'N': '229'},
        'Name': {'S': 'Mansi'},
        'Surname': {'S': 'Gawade'},
        'Cgpa': {'N': '9.90'},
        'Age': {'N': '20'}
    },
    {
        'Roll NO': {'N': '237'},
        'Name': {'S': 'Rohit'},
        'Surname': {'S': 'Patil'},
        'Cgpa': {'N': '7.90'},
        'Age': {'N': '23'}
    },
    {
        'Roll NO': {'N': '226'},
        'Name': {'S': 'Yash'},
        'Surname': {'S': 'Shinde'},
        'Cgpa': {'N': '6.90'},
        'Age': {'N': '22'}
    },
]

# Put each item into the table
for item in items:
    try:
        dynamodb_client.put_item(TableName=table_name, Item=item)
        print("Item added successfully.")
    except Exception as e:
        print(f"An error occurred while putting item into table '{table_name}': {e}")
