#!/usr/bin/python3
import boto3
import sys

region = "us-east-2"

def stop_instances(region):
    ec2 = boto3.client('ec2', region_name=region)

    filters = [
      {'Name': 'instance-state-name', 'Values': ['running']},
      {'Name': 'tag:Type', 'Values': ['temporary']}
    ]

    response = ec2.describe_instances(Filters=filters)

    instances_ids = []

    for reserv in response['Reservations']:
        for instance in reserv['Instances']:
            instances_ids.append(instance['InstanceId'])
            print(instances_ids)
        if instances_ids:
            ec2.stop_instances(InstanceIds=instances_ids)
            print(f"Stopped {len(instances_ids)} in {region}")
        else:
            print(f"Not found temporary instances in {region}")

def start_by_name(region, name):
    ec2 = boto3.client('ec2', region_name=region)
    response = ec2.describe_instances()
    instances_ids = []
    for reserv in response['Reservations']:
        for instance in reserv['Instances']:
            if instance['State']['Name'] == 'running':
                continue
            for tag in instance.get('Tags', []):
                if tag['Key'] == 'Name' and tag['Value'] == name:
                    instances_ids.append(instance['InstanceId'])
                    break
    if instances_ids:
        ec2.start_instances(InstanceIds=instances_ids)
        print(f"Started instance: {name}")
    else:
        print(f"Not foud stopped instance {name}")

if __name__ == "__main__":
    action = sys.argv[1]
    region = sys.argv[2]
    if action == 'stop':
        stop_instances(region)
    elif action == 'start':
        name = sys.argv[3]
        start_by_name(region, name)
    else:
        print("Incorrect action or region")
        sys.exit(1)
