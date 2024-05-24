import boto3

# Create a client for RDS
client = boto3.client('rds')

response = client.create_db_snapshot(
    DBInstanceIdentifier='mymysqlinstance',
    DBSnapshotIdentifier='mydbsnapshot',
)

print("DB snapshot creation initiated successfully.")