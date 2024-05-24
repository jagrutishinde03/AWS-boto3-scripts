import boto3

# Create a client for RDS
client = boto3.client('rds')

response = client.describe_db_log_files(
    DBInstanceIdentifier='mymysqlinstance',
    FileLastWritten=1470873600000,
    FileSize=0,
    FilenameContains='error',
)

print(response)