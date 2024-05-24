import boto3

# Create a client for RDS
client = boto3.client('rds')

response = client.delete_db_instance(
    DBInstanceIdentifier='mymysqlinstance',
    SkipFinalSnapshot=True,
)
print("DB deleted successfully.")
print(response)