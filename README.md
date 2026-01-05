<div align="center">

# ⚡ AWS Ops CLI

<img src="https://img.shields.io/badge/AWS-EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white" alt="AWS EC2"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge" alt="MIT License"/>
<img src="https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge" alt="Version"/>

### _A lightning-fast, terminal-first AWS EC2 management tool_

**Built for DevOps engineers who value speed, safety, and simplicity**

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Roadmap](#-roadmap)

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>

---

## 🎯 Why AWS Ops CLI?

<table>
<tr>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257472-08e52665-c503-4bd9-aa20-f5a4dae769b5.gif" width="80">
<h3>⚡ Lightning Fast</h3>
<p>Manage EC2 instances in seconds, not minutes. No more console clicking.</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257468-1e9a91f1-b626-4baa-b15d-5c385dfa7ed2.gif" width="80">
<h3>🛡️ Safe by Default</h3>
<p>Built-in confirmations for destructive actions. Multi-account aware.</p>
</td>
<td width="33%" align="center">
<img src="https://user-images.githubusercontent.com/74038190/212257465-7ce8d493-cac5-494e-982a-5a9deb852c4b.gif" width="80">
<h3>🎨 Beautiful UX</h3>
<p>Color-coded output, clean tables, and intuitive commands.</p>
</td>
</tr>
</table>

---

## ✨ Features

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

---

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=for-the-badge&logo=amazon-aws&logoColor=white)

**Core Dependencies:** `boto3` • `argparse` • `tabulate` • `colorama`

</div>

---

## 📥 Installation

### Prerequisites

<img src="https://user-images.githubusercontent.com/74038190/212257454-16e3712e-945a-4ca2-b238-408ad0bf87e6.gif" width="50" align="left">

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

---

## 🚀 Usage

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

---

## 📸 Screenshots

<div align="center">

### 📊 Instance List View

_Clean, color-coded table showing all your EC2 instances_

<img src="screenshots/list.png" alt="List View" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

<br><br>

### 🔍 Instance Status

_Comprehensive details about a specific instance_

<img src="screenshots/status.png" alt="Status View" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

<br><br>

### ⏹️ Stop Confirmation

_Safety-first: Confirmation prompt for destructive actions_

<img src="screenshots/stop.png" alt="Stop Confirmation" width="800" style="border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"/>

</div>

> 📸 **How to capture screenshots:**
>
> ```bash
> mkdir screenshots
> aws-ops list                      # Screenshot as list.png
> aws-ops status i-0abc123          # Screenshot as status.png
> aws-ops stop i-0abc123            # Screenshot as stop.png
> ```

---

## 🧠 Design Philosophy

<img src="https://user-images.githubusercontent.com/74038190/212284158-e840e285-664b-44d7-b79b-e264b5e54825.gif" width="400" align="right">

**Safe by Default**

- No bulk destructive operations
- Confirmation prompts for critical actions
- Clear error messages

**Developer Experience**

- Intuitive command structure
- Consistent output formatting
- Helpful error handling

**Production Ready**

- Multi-account support
- Region awareness
- Graceful AWS error handling

<br clear="right"/>

## 🤝 Contributing

<div align="center">

**Contributions are welcome!**

<img src="https://user-images.githubusercontent.com/74038190/212284087-bbe7e430-757e-4901-90bf-4cd2ce3e1852.gif" width="200">

</div>

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

<div align="center">

<img src="https://user-images.githubusercontent.com/74038190/212284136-03988914-d899-44b4-b1d9-4eeccf656e44.gif" width="150">

### **Shashank**

_DevOps & Cloud Enthusiast_

[![GitHub](https://img.shields.io/badge/GitHub-itsiiie-181717?style=for-the-badge&logo=github)](https://github.com/itsiiie)
[![AWS](https://img.shields.io/badge/AWS-Certified-FF9900?style=for-the-badge&logo=amazon-aws)](https://github.com/itsiiie)

**Expertise:** AWS • Docker • CI/CD • Automation • Infrastructure as Code

</div>

---

## 📜 License

<div align="center">

MIT License - feel free to use this project for personal or commercial purposes

Copyright © 2024 Shashank

<img src="https://user-images.githubusercontent.com/74038190/212284115-f47cd8ff-2ffb-4b04-b5bf-4d1c14c0247f.gif" width="200">

</div>

---

<div align="center">

### ⭐ Star this repo if you find it useful!

**Made with ❤️ for the DevOps Community**

<img src="https://user-images.githubusercontent.com/74038190/212284100-561aa473-3905-4a80-b561-0d28506553ee.gif" width="700">

</div>
