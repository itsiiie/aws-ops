import argparse

from aws_ops.ec2 import (
    list_instances,
    start_instance,
    stop_instance,
    get_instance_status,
)


def confirm_action(message: str) -> bool:
    choice = input(f"{message} (y/N): ").strip().lower()
    return choice in ["y", "yes"]


def run():
    parser = argparse.ArgumentParser(
        description="AWS Ops CLI – Version 1 (EC2 Management)"
    )

    # Global option
    parser.add_argument(
        "--region",
        help="AWS region (e.g. ap-south-1, us-east-1)"
    )

    subparsers = parser.add_subparsers(dest="command")

    # -------- list --------
    subparsers.add_parser(
        "list",
        help="List EC2 instances"
    )

    # -------- start --------
    start_cmd = subparsers.add_parser(
        "start",
        help="Start an EC2 instance"
    )
    start_cmd.add_argument("instance_id")

    # -------- stop --------
    stop_cmd = subparsers.add_parser(
        "stop",
        help="Stop an EC2 instance"
    )
    stop_cmd.add_argument("instance_id")

    # -------- status --------
    status_cmd = subparsers.add_parser(
        "status",
        help="Show detailed EC2 instance status"
    )
    status_cmd.add_argument("instance_id")

    args = parser.parse_args()

    # ================= COMMAND HANDLERS =================

    if args.command == "list":
        instances = list_instances(args.region)

        print(
            f"{'ID':<25} {'NAME':<20} {'STATE':<10} "
            f"{'TYPE':<10} {'AZ':<12} {'PUBLIC_IP':<15}"
        )
        print("-" * 100)

        for i in instances:
            print(
                f"{i['id']:<25} {i['name']:<20} {i['state']:<10} "
                f"{i['type']:<10} {i['az']:<12} {i['public_ip']:<15}"
            )

    elif args.command == "start":
        success, msg = start_instance(
            args.instance_id, args.region
        )
        print(("✔" if success else "❌"), msg)

    elif args.command == "stop":
        if not confirm_action(
            f"Are you sure you want to STOP instance {args.instance_id}?"
        ):
            print("❌ Operation cancelled")
            return

        success, msg = stop_instance(
            args.instance_id, args.region
        )
        print(("✔" if success else "❌"), msg)

    elif args.command == "status":
        success, data = get_instance_status(
            args.instance_id, args.region
        )

        if not success:
            print("❌", data)
            return

        print(f"Instance ID : {data['id']}")
        print(f"Name        : {data['name']}")
        print(f"State       : {data['state']}")
        print(f"Type        : {data['type']}")
        print(f"AZ          : {data['az']}")
        print(f"Platform    : {data['platform']}")
        print(f"Private IP  : {data['private_ip']}")
        print(f"Public IP   : {data['public_ip']}")
        print(f"Launch Time : {data['launch_time']}")

    else:
        parser.print_help()
