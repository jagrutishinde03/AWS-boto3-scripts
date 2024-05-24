
# AWS Boto3 Scripts

This repository contains various Python scripts to interact with AWS services using the Boto3 library. The scripts cover a range of AWS services including DynamoDB, RDS, EC2, and S3.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Scripts](#scripts)
  - [DynamoDB](#dynamodb)
  - [RDS](#rds)
  - [EC2](#ec2)
  - [S3](#s3)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## Installation

To use these scripts, you need to have Python 3 and Boto3 installed. You can install Boto3 using pip:

```bash
pip install boto3
```

## Usage

Each script is designed to perform specific tasks on AWS services. Before running the scripts, ensure that your AWS credentials are properly configured. You can configure your AWS credentials using the AWS CLI:

```bash
aws configure
```

Alternatively, you can set the credentials as environment variables:

```bash
export AWS_ACCESS_KEY_ID='your-access-key-id'
export AWS_SECRET_ACCESS_KEY='your-secret-access-key'
export AWS_DEFAULT_REGION='your-default-region'
```

## Scripts

### DynamoDB

Scripts for interacting with DynamoDB, including creating tables, inserting items, querying, and deleting tables.

- `create_table.py`: Script to create a DynamoDB table.
- `delete_item.py`: Script to delete an item from a DynamoDB table.
- `delete_table.py`: Script to delete a DynamoDB table.
- `describe_table.py`: Script to describe a DynamoDB table.
- `get_item.py`: Script to get an item from a DynamoDB table.
- `put_item.py`: Script to insert an item into a DynamoDB table.
- `query.py`: Script to query items from a DynamoDB table.
- `scan.py`: Script to scan items in a DynamoDB table.
- `update_item.py`: Script to update an item in a DynamoDB table.

### RDS

Scripts for managing RDS instances, such as creating, describing, modifying, and deleting instances.

- `create_rds.py`: Script to create an RDS instance.
- `db_snapshot.py`: Script to create a snapshot of an RDS instance.
- `delete_db.py`: Script to delete an RDS instance.
- `describe_log.py`: Script to describe logs for an RDS instance.
- `modify.py`: Script to modify an RDS instance.

### EC2

Scripts for managing EC2 instances, including launching, describing, stopping, and terminating instances.

- `launch_instance.py`: Script to launch an EC2 instance.
- `describe_instances.py`: Script to describe EC2 instances.
- `stop_instance.py`: Script to stop an EC2 instance.
- `terminate_instance.py`: Script to terminate an EC2 instance.

### S3

Scripts for interacting with S3, such as creating buckets, uploading files, listing buckets, and deleting objects.

- `create_bucket.py`: Script to create an S3 bucket.
- `upload_file.py`: Script to upload a file to an S3 bucket.
- `list_buckets.py`: Script to list all S3 buckets.
- `delete_object.py`: Script to delete an object from S3 bucket.
- `delete_bucket.py`: Script to delete an bucket from S3.

## Configuration

Ensure your AWS credentials and region are configured before running the scripts. You can configure these using the AWS CLI or by setting environment variables as described in the [Usage](#usage) section.

## Contributing

Contributions are welcome! Please fork this repository and submit pull requests with your changes. Make sure to follow the existing code style and include detailed commit messages.

## License

This project is licensed under the MIT License. 
