import boto3

client = boto3.client('ec2')

response = client.describe_instances(
    InstanceIds=[
        'i-0d019ba10cbf75f72',
    ],
)

print(response)