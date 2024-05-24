import boto3

# Create a client for RDS
client = boto3.client('rds')

response = client.modify_db_instance(
    AllocatedStorage=10,
    ApplyImmediately=True,
    BackupRetentionPeriod=1,
    DBInstanceClass='db.t2.small',
    DBInstanceIdentifier='mymysqlinstance',
    MasterUserPassword='mynewpassword',
    PreferredBackupWindow='04:00-04:30',
    PreferredMaintenanceWindow='Tue:05:00-Tue:05:30',
)
print("DB modification initiated successfully.")