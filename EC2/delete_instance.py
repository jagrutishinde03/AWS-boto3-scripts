import boto3

# Create a boto3 client for EC2
ec2_client = boto3.client('ec2')

# Prompt the user to enter the name of the instance to delete
instance_name = input("Enter the name of the instance to delete: ")

# Describe instances to find the instance ID
response = ec2_client.describe_instances(Filters=[{'Name': 'tag:Name', 'Values': [instance_name]}])

# Extract the instance ID(s) from the response
instance_ids = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_ids.append(instance['InstanceId'])

# Delete the instance(s)
if instance_ids:
    ec2_client.terminate_instances(InstanceIds=instance_ids)
    print(f"Instance(s) with name '{instance_name}' are being terminated.")
else:
    print(f"No instance found with name '{instance_name}'.")
