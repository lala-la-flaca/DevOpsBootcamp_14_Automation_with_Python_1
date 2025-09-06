# 🐍Module 14 – Automation with Python
This exercise is part of Module 14: Automation with Python. Module 14 focuses on automating cloud operations with Python. The demos showcase how to interact with AWS services (EC2, EKS, snapshots), perform monitoring tasks, and implement recovery workflows. By the end of this module, you will have practical experience in scripting infrastructure automation, monitoring, and recovery solutions.

# 📦Demo 1 – Health Check: EC2 Status Checks
# 📌 Objective
Create a Python script to fetch and display EC2 instance statuses and extend it to run checks at regular intervals.

# 🚀 Technologies Used
* Python: programming language.
* IntelliJ-PyCharm: IDE used for development.
* AWS: Cloud provider.
* Boto3 AWS SDK for Python.
* Terraform: Infrastructure provisioning tool.
  
# 🎯 Features
☁️ Create EC2 instances using Terraform.

✅ Fetch EC2 instance statuses

🔄 Continuous status monitoring with intervals

# Prerequisites
* AWS account
* Terraform from previous Demos.
* Python and PyCharm installed.
  
# 🏗 Project Architecture

# ⚙️ Project Configuration
## Infraestructure with Terraform
1. Use Terraform to provision EC2 instances using the initial Terraform Demo1.
2. Modify the Terraform file to add the second and third instances.
3. Plan and test infrastructure using Terraform.
4. Deploy infrastructure with Terraform
5. Check the AWS console to check components.
   
## Monitoring Instances
1. Install the boto3 SDK for AWS
2. Initialize the client and resource
3. Obtain the current status of EC2 instances.
4. Output Results
