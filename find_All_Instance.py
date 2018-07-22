import boto3

client = boto3.client('ec2')
All_Region = []

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

print("Running and Stopped Instance : {}".format(All_Instance))
