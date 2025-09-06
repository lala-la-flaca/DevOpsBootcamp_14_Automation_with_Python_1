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
   [Terraform files](https://gitlab.com/devopsbootcamp4095512/devopsbootcamp_12_terraform_aws/-/tree/demo/python-and-terraform?ref_type=heads)
   
2. Modify the Terraform file to add the second and third instances.
   ```bash
      # Creating EC2 2
      resource "aws_instance" "myapp-ec2-2" {
        ami           = data.aws_ami.Lastest-Amazon-Linux-image.id
        instance_type = var.instance_type
      
        #Assigning the subnet
        subnet_id = aws_subnet.myapp-subnet-1.id
      
        #Assiging the Ec2 to a SG
        vpc_security_group_ids = [aws_security_group.myapp-sg.id]
      
        #Assigning availability_zone
        availability_zone = var.avail_zone
      
        #Assigning a public IP
        associate_public_ip_address =  true
      
        #Associating SSH key
        key_name = aws_key_pair.ssh-key.key_name
      
        tags = {
          Name = "${var.env_prefix}-myapp-server-ec2-2"
        }
      
        user_data = file("user_data_bootstrap.sh")
      
      #This ensures that every time the user data bootstrap is modified, the EC2 is destroyed and recreated
      user_data_replace_on_change = true
      }
   ```
   
3. Plan and test infrastructure using Terraform.
   ```bash
   terraform plan
   ```
4. Deploy infrastructure with Terraform
   ```bash
   terraform apply
   ```
5. Check the AWS console to check components.
   <img src="" width=800 />
   
## Monitoring Instances
1. Install the boto3 SDK for AWS
   ```
    pip install boto3
   ```
   [Boto Module](https://pypi.org/project/boto3/)

   
2. Import library
   ```bash
   import boto3
   ```
4. Initialize the EC2 client.
   ```bash
   ec2_client = boto3.client('ec2', region_name="us-east-1")
   ```
   <img src="" />
   
6. Check Available EC2 instances
   ```bash
      #Getting All EC2 instances available in region US-EAST-1
      #Using describe instance
      all_available_instances = ec2_client.describe_instances()
   ```
8. Obtain the current status of EC2 instances.
   ```bash
     def check_instance_status():
      #Using describe instance status
      #Getting All instance statuses
      all_instance_statuses = ec2_client.describe_instance_status(
          IncludeAllInstances=True
          #Dedefault behavior returns only running instances, when setting this parameters to True, then includes all states
      )
      instance_statuses =  all_instance_statuses["InstanceStatuses"]
  
      for instance_status in instance_statuses:
          instance_id =  instance_status["InstanceId"]
          instance_state = instance_status["InstanceState"]["Name"]
          ec2_status = instance_status["InstanceStatus"]["Status"]
          system_status = instance_status['SystemStatus']["Status"]
          print(f"Instance {instance_id} is {instance_state} with instance Status:{ec2_status} & System Status:{system_status}")
      print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

   ```
9. Import Schedule module
  ```bash
  import schedule  
  ```
11. Schedule the app to check the EC2 status every 10 seconds ( Demo purposes only)
    ```bash
    schedule.every(10).seconds.do(check_instance_status)
    while True:
    schedule.run_pending()
    ```
12. Output Results
    <img src="" />

    
