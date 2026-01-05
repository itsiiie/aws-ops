import boto3
from botocore.exceptions import ClientError


def ec2_client(region=None):
    if region:
        return boto3.client("ec2", region_name=region)
    return boto3.client("ec2")


def list_instances(region=None):
    ec2 = ec2_client(region)
    response = ec2.describe_instances()

    instances = []

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:

            # Extract Name tag
            name = "-"
            for tag in instance.get("Tags", []):
                if tag["Key"] == "Name":
                    name = tag["Value"]

            instances.append({
                "id": instance["InstanceId"],
                "name": name,
                "state": instance["State"]["Name"],
                "type": instance["InstanceType"],
                "az": instance["Placement"]["AvailabilityZone"],
                "private_ip": instance.get("PrivateIpAddress", "-"),
                "public_ip": instance.get("PublicIpAddress", "-"),
                "platform": instance.get("Platform", "Linux/Unix"),
                "launch_time": instance["LaunchTime"].strftime("%Y-%m-%d %H:%M"),
            })

    return instances


def start_instance(instance_id, region=None):
    ec2 = ec2_client(region)
    try:
        ec2.start_instances(InstanceIds=[instance_id])
        return True, f"Instance {instance_id} is starting"
    except ClientError as e:
        return False, e.response["Error"]["Message"]


def stop_instance(instance_id, region=None):
    ec2 = ec2_client(region)
    try:
        ec2.stop_instances(InstanceIds=[instance_id])
        return True, f"Instance {instance_id} is stopping"
    except ClientError as e:
        return False, e.response["Error"]["Message"]


def get_instance_status(instance_id, region=None):
    ec2 = ec2_client(region)
    try:
        response = ec2.describe_instances(InstanceIds=[instance_id])
        instance = response["Reservations"][0]["Instances"][0]

        name = "-"
        for tag in instance.get("Tags", []):
            if tag["Key"] == "Name":
                name = tag["Value"]

        return True, {
            "id": instance["InstanceId"],
            "name": name,
            "state": instance["State"]["Name"],
            "type": instance["InstanceType"],
            "az": instance["Placement"]["AvailabilityZone"],
            "private_ip": instance.get("PrivateIpAddress", "-"),
            "public_ip": instance.get("PublicIpAddress", "-"),
            "platform": instance.get("Platform", "Linux/Unix"),
            "launch_time": instance["LaunchTime"].strftime("%Y-%m-%d %H:%M"),
        }

    except ClientError as e:
        return False, e.response["Error"]["Message"]
    except Exception as e:
        return False, str(e)
