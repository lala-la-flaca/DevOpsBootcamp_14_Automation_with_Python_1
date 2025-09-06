import  boto3
import schedule

ec2_client = boto3.client('ec2', region_name="us-east-1")

#Getting All EC2 instances available in region US-EAST-1
#Using describe instance
all_available_instances = ec2_client.describe_instances()
#print(type(all_available_instances))
#print(all_available_instances)

#Getting Reservations to access EC2 instances available
"""
reservations = all_available_instances["Reservations"]
for reservation in reservations:
    instances = reservation['Instances']
    for instance in instances:

        #EC2 Instance parameters
        ec2_id = instance["InstanceId"]
        ec2_state = instance["State"]["Name"]
        print (f"This is the current status of the EC2 intance:\nEC2 id: {ec2_id}\nEC2 State:{ec2_state}")
"""
def check_instance_status():
    #Using describe instance status
    #Getting All instance statuses
    all_instance_statuses = ec2_client.describe_instance_status(
        IncludeAllInstances=True
        #Dedefault behavior returns only running instances, when setting this parameter to True, then includes all states
    )
    instance_statuses =  all_instance_statuses["InstanceStatuses"]

    for instance_status in instance_statuses:
        instance_id =  instance_status["InstanceId"]
        instance_state = instance_status["InstanceState"]["Name"]
        ec2_status = instance_status["InstanceStatus"]["Status"]
        system_status = instance_status['SystemStatus']["Status"]
        print(f"Instance {instance_id} is {instance_state} with instance Status:{ec2_status} & System Status:{system_status}")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-\n")

schedule.every(10).seconds.do(check_instance_status)

while True:
    schedule.run_pending()