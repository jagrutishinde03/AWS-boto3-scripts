import boto3

# Create a client for RDS
client = boto3.client('rds')

# Define parameters for creating RDS instance
response = client.create_db_instance(
    AllocatedStorage=5,
    DBInstanceClass='db.r6g.2xlarge',  # Change instance class to a supported one
    DBInstanceIdentifier='mymysqlinstance',
    Engine='MySQL',  # Lowercase engine name
    EngineVersion='8.0.35',  # Choose a supported MySQL engine version
    LicenseModel='general-public-license',
    MasterUsername='MyUser',
    MasterUserPassword='MyPassword',
)

print("DB creation initiated successfully.")
