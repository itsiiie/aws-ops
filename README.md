<div align="center">

<!-- Animated Header -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=AWS%20Ops%20CLI&fontSize=80&fontAlignY=35&animation=twinkling&fontColor=fff" width="100%"/>

# ⚡ AWS Ops CLI

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&duration=3000&pause=1000&color=F75C7E&center=true&vCenter=true&multiline=true&width=800&height=100&lines=Lightning-Fast+Terminal-First+AWS+EC2+Management;Built+for+DevOps+Engineers;Speed+%E2%9A%A1+Safety+%F0%9F%9B%A1%EF%B8%8F+Simplicity+%F0%9F%8E%A8" alt="Typing SVG" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS EC2"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="MIT License"/>
<img src="https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge" alt="Version"/>
</p>

<p align="center">
  <a href="#-features">Features</a> •
  <a href="#-installation">Installation</a> •
  <a href="#-usage">Usage</a> •
  <a href="#-screenshots">Screenshots</a> •
  <a href="#-roadmap">Roadmap</a>
</p>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

<br>

<!-- Divider with Gradient -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 🎯 Why AWS Ops CLI?

<div align="center">

<table>
<tr>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="100">
<br><br>
<h3>⚡ Lightning Fast</h3>
<p>Manage EC2 instances in seconds, not minutes. No more console clicking.</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="100">
<br><br>
<h3>🛡️ Safe by Default</h3>
<p>Built-in confirmations for destructive actions. Multi-account aware.</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="100">
<br><br>
<h3>🎨 Beautiful UX</h3>
<p>Color-coded output, clean tables, and intuitive commands.</p>
</td>
</tr>
</table>

</div>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## ✨ Features

<div align="center">

<details open>
<summary><b>📋 Core Capabilities</b></summary>

<br>

| Feature                 | Description                                    | Status  |
| ----------------------- | ---------------------------------------------- | ------- |
| 📊 **List Instances**   | Display all EC2 instances in a beautiful table | ✅ Live |
| ▶️ **Start Instances**  | Boot up instances with a single command        | ✅ Live |
| ⏹️ **Stop Instances**   | Safely stop instances (with confirmation)      | ✅ Live |
| 🔍 **Instance Details** | View comprehensive instance information        | ✅ Live |
| 🌍 **Multi-Region**     | Switch between AWS regions seamlessly          | ✅ Live |
| 👤 **Multi-Profile**    | Support for multiple AWS accounts              | ✅ Live |
| 🎨 **Colored Output**   | Clear state indicators and visual feedback     | ✅ Live |

</details>

<details>
<summary><b>🔮 Coming Soon (v2.0)</b></summary>

<br>

- ⏰ **Scheduler** - Auto start/stop instances on schedule
- 💰 **Cost Tracking** - Monitor EC2 spending in real-time
- 🗄️ **S3 Support** - Manage S3 buckets from CLI
- 🗃️ **RDS Support** - Control RDS databases
- 📝 **Verbose Logging** - Detailed operation logs
- 📊 **Usage Analytics** - Track your AWS resource usage

</details>

</div>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 🛠️ Tech Stack

<div align="center">

<img src="https://skillicons.dev/icons?i=python,aws&theme=dark" />

<br><br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

**Core Dependencies:** `boto3` • `argparse` • `tabulate` • `colorama`

</div>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 📥 Installation

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="100">
</div>

### Prerequisites

<br>

- Python 3.8 or higher
- AWS credentials configured
- Active AWS account

<br clear="left"/>

### Quick Install

```bash
# Clone the repository
git clone https://github.com/itsiiie/aws-ops.git
cd aws-ops

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install the CLI
pip install -e .
```

### Configure AWS Credentials

```bash
aws configure
```

**Required inputs:**

- AWS Access Key ID
- AWS Secret Access Key
- Default region (e.g., `us-east-1`, `ap-south-1`)
- Output format (recommended: `json`)

> 💡 **Tip:** For multiple AWS accounts, use named profiles with `aws configure --profile <name>`

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 🚀 Usage

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257467-871d32b7-e401-42e8-a166-fcfd7baa4c6b.gif" width="100">
</div>

### Basic Commands

<table>
<tr>
<td width="50%">

**📋 List all EC2 instances**

```bash
aws-ops list
```

**With specific region:**

```bash
aws-ops --region ap-south-1 list
```

**With AWS profile:**

```bash
aws-ops --profile production list
```

</td>
<td width="50%">

**▶️ Start an instance**

```bash
aws-ops start i-0abc123def456
```

**⏹️ Stop an instance**

```bash
aws-ops stop i-0abc123def456
```

_Includes safety confirmation prompt_

**🔍 Get instance details**

```bash
aws-ops status i-0abc123def456
```

</td>
</tr>
</table>

### Advanced Examples

```bash
# Multi-region deployment check
aws-ops --region us-east-1 list
aws-ops --region eu-west-1 list
aws-ops --region ap-south-1 list

# Multi-account management
aws-ops --profile dev start i-dev123
aws-ops --profile staging start i-staging456
aws-ops --profile prod start i-prod789

# Detailed instance inspection
aws-ops --region us-west-2 --profile production status i-0abc123
```

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 📸 Screenshots

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212257463-4d82cb45-7b75-4ce7-a358-bc52192a574a.gif" width="100">

<br><br>

### 📊 Instance List View

_Clean, color-coded table showing all your EC2 instances_

<br>

<img src="screenshots/list.png" alt="List View" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

<br><br>

### 🔍 Instance Status

_Comprehensive details about a specific instance_

<br>

<img src="screenshots/status.png" alt="Status View" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

<br><br>

### ⏹️ Stop Confirmation

_Safety-first: Confirmation prompt for destructive actions_

<br>

<img src="screenshots/stop-confirm.png" alt="Stop Confirmation" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

</div>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 🧠 Design Philosophy

<div align="center">
<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400">
</div>

<br>

<table>
<tr>
<td width="33%" align="center">

**Safe by Default**

- No bulk destructive operations
- Confirmation prompts for critical actions
- Clear error messages

</td>
<td width="33%" align="center">

**Developer Experience**

- Intuitive command structure
- Consistent output formatting
- Helpful error handling

</td>
<td width="33%" align="center">

**Production Ready**

- Multi-account support
- Region awareness
- Graceful AWS error handling

</td>
</tr>
</table>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 🤝 Contributing

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="200">

<br>

**Contributions are welcome!**

</div>

<br>

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 👨‍💻 Author

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="150">

<br>

### **Shashank**

_DevOps & Cloud Enthusiast_

<br>

[![GitHub](https://img.shields.io/badge/GitHub-itsiiie-181717?style=for-the-badge&logo=github)](https://github.com/itsiiie)
[![AWS](https://img.shields.io/badge/AWS-Certified-FF9900?style=for-the-badge&logo=amazon-aws)](https://github.com/itsiiie)

<br>

**Expertise:** AWS • Docker • CI/CD • Automation • Infrastructure as Code

</div>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

## 📜 License

<div align="center">

MIT License - feel free to use this project for personal or commercial purposes

Copyright © 2024 Shashank

<br><br>

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="200">

</div>

<br>

<!-- Divider -->
<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="100%">

<br>

<div align="center">

### ⭐ Star this repo if you find it useful!

<a href="https://github.com/itsiiie/aws-ops/stargazers">
<img src="https://img.shields.io/github/stars/itsiiie/aws-ops?style=social" alt="GitHub stars">
</a>

<br><br>

**Made with ❤️ for the DevOps Community**

<br><br>

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

<br>

<!-- Animated Footer -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

</div>
