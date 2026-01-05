# AWS Ops CLI

A lightweight command-line tool to manage AWS EC2 instances without opening the AWS Console.

## Features (v1)

- List EC2 instances
- Start EC2 instance
- Stop EC2 instance (with confirmation)
- View detailed instance status
- Region-aware commands

## Installation

```bash
git clone <repo-url>
cd aws-ops-cli
pip install -e .
```

# Usage

```bash
aws-ops list
aws-ops --region ap-south-1 status i-0abc123
aws-ops stop i-0abc123 --region ap-south-1
```

# Requirements

- Python 3.8+
- AWS CLI configured
