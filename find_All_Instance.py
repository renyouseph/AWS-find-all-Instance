###############################
#
#This scipt is used to find all instances (Running/Stopped) from all regions
<<<<<<< HEAD
#It dispays result in a PyTable
#
##### Server Requirements ####################
# Python        # apt-get install python3
# apt-get install libssl-dev -y
# Pip           # apt-get install -y python3-pip
# AWS CLI       # pip3 install awscli , # aws configure
# Boto3         # pip install boto3
# PrettyTable   # pip3 install PrettyTable
=======
#It dispays Instane_ID, Instance_type, Instance_state
#
##### Server Requirements ####################
# Python    # apt-get install python3
# apt-get install libssl-dev -y
# Pip     - # apt-get install -y python3-pip
# AWS CLI - # pip3 install awscli , # aws configure
# Boto3   - # pip install boto3
>>>>>>> 2fd20708be30f66ec650501cf1b2805ca47de0b2
##############################################
#
# Written by Reny Ouseph
# renyouseph@gmail.com +91 9072997607
#
##############################################


import boto3

client = boto3.client('ec2')
All_Region = []

################# Taking all regions ID #############

for region in client.describe_regions()['Regions']:
        All_Region.append(region['RegionName'])

All_Instance = {}

for REGION in All_Region:
    ec2Resource = boto3.resource('ec2',region_name=REGION)
    instances = ec2Resource.instances.filter()
    for instance in instances:
        if instance.state["Name"] == "running":
            if REGION not in All_Instance:
                All_Instance[REGION] =[]
                All_Instance[REGION].append({'Inastance_ID':'{}'.format(instance.id),'Inastance_type':'{}'.format(instance.instance_type),\
                                             'Inastance_state':'{}'.format(instance.state["Name"])})
            else:
                All_Instance[REGION].append({'Inastance_ID':'{}'.format(instance.id),'Inastance_type':'{}'.format(instance.instance_type),\
                                             'Inastance_state':'{}'.format(instance.state["Name"])})
        if instance.state["Name"] == "stopped":
            if REGION not in All_Instance:
                All_Instance[REGION] =[]
                All_Instance[REGION].append({'Inastance_ID':'{}'.format(instance.id),'Inastance_type':'{}'.format(instance.instance_type),\
                                             'Inastance_state':'{}'.format(instance.state["Name"])})
            else:
                All_Instance[REGION].append({'Inastance_ID':'{}'.format(instance.id),'Inastance_type':'{}'.format(instance.instance_type),\
                                             'Inastance_state':'{}'.format(instance.state["Name"])})

<<<<<<< HEAD
#print("Running and Stopped Instance : {}".format(All_Instance))  ### Please uncomment this line if you need a detailed result.

print("")
print("")


from prettytable import PrettyTable
result = PrettyTable()
result.field_names = ["Region","Total_Instance","Running","Stopped"]


for region in All_Instance.keys():
    running_count = 0
    stopped_count = 0
    total_count = 0
    for values in All_Instance[region]:
        if values['Inastance_state'] == 'running':
            running_count = running_count+1
        if values['Inastance_state'] == 'stopped':
            stopped_count = stopped_count+1
    total_count = running_count + stopped_count
    result.add_row([region,total_count,running_count,stopped_count])
print(result)
=======
print("Running and Stopped Instance : {}".format(All_Instance))
>>>>>>> 2fd20708be30f66ec650501cf1b2805ca47de0b2
