import boto3

# Create a boto3 client for EC2
ec2_client = boto3.client('ec2')

# Prompt the user to enter the name for the instance
instance_name = input("Enter the name for the instance: ")

# Specify the parameters for the instance
instance_params = {
    'ImageId': 'ami-07caf09b362be10b8',         # Specify the AMI ID of the instance
    'InstanceType': 't2.micro',        # Specify the instance type (e.g., t2.micro)
    'KeyName': 'Ecom-ec2-keypair',   # Specify the key pair name for SSH access
    'MaxCount': 1,                      # Specify the maximum number of instances to launch
    'MinCount': 1,                      # Specify the minimum number of instances to launch
    'TagSpecifications': [{
        'ResourceType': 'instance',
        'Tags': [{'Key': 'Name', 'Value': instance_name}]
    }]
    # Add other parameters as needed, such as SecurityGroupIds, SubnetId, etc.
}

# Launch the instance
response = ec2_client.run_instances(**instance_params)

# Extract the instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

# Print the instance ID
print("Instance ID:", instance_id)
