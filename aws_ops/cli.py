import argparse

from tabulate import tabulate
from colorama import Fore, Style, init

from aws_ops.ec2 import (
    list_instances,
    start_instance,
    stop_instance,
    get_instance_status,
)

# initialize colorama
init(autoreset=True)


# ----------------- Helper Functions -----------------

def confirm_action(message: str) -> bool:
    choice = input(f"{message} (y/N): ").strip().lower()
    return choice in ["y", "yes"]


def color_state(state: str) -> str:
    if state == "running":
        return Fore.GREEN + "🟢 running" + Style.RESET_ALL
    if state == "stopped":
        return Fore.RED + "🔴 stopped" + Style.RESET_ALL
    return Fore.YELLOW + f"🟡 {state}" + Style.RESET_ALL


def success(msg: str):
    print(Fore.GREEN + "✔ " + msg + Style.RESET_ALL)


def error(msg: str):
    print(Fore.RED + "❌ " + msg + Style.RESET_ALL)


# ----------------- CLI Entry -----------------

def run():
    parser = argparse.ArgumentParser(
        description="AWS Ops CLI – Version 1 (EC2 Management)"
    )

    # Global argument
    parser.add_argument(
        "--region",
        help="AWS region (example: ap-south-1, us-east-1)"
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

        table = []
        for i in instances:
            table.append([
                i["id"],
                i["name"],
                color_state(i["state"]),
                i["type"],
                i["az"],
                i["public_ip"],
            ])

        print(
            tabulate(
                table,
                headers=[
                    "Instance ID",
                    "Name",
                    "State",
                    "Type",
                    "AZ",
                    "Public IP",
                ],
                tablefmt="grid",
            )
        )

    elif args.command == "start":
        success_flag, msg = start_instance(
            args.instance_id, args.region
        )
        success(msg) if success_flag else error(msg)

    elif args.command == "stop":
        if not confirm_action(
            f"Are you sure you want to STOP instance {args.instance_id}?"
        ):
            error("Operation cancelled")
            return

        success_flag, msg = stop_instance(
            args.instance_id, args.region
        )
        success(msg) if success_flag else error(msg)

    elif args.command == "status":
        success_flag, data = get_instance_status(
            args.instance_id, args.region
        )

        if not success_flag:
            error(data)
            return

        print(f"Instance ID : {data['id']}")
        print(f"Name        : {data['name']}")
        print(f"State       : {color_state(data['state'])}")
        print(f"Type        : {data['type']}")
        print(f"AZ          : {data['az']}")
        print(f"Platform    : {data['platform']}")
        print(f"Private IP  : {data['private_ip']}")
        print(f"Public IP   : {data['public_ip']}")
        print(f"Launch Time : {data['launch_time']}")

    else:
        parser.print_help()
