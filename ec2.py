import logging
import boto3
from botocore.exceptions import ClientError

ec2 = boto3.resource('ec2',region_name='ap-south-1')   

def create_security_g():
    try:
         
        response = ec2.create_security_group(GroupName='Boto3Sec',
                                        Description='Boto3Sec',
                                        VpcId = 'vpc-4edec626')
        security_group_id = response.__dict__['_id']
                    
        response = response.authorize_ingress(
            GroupId=security_group_id,
            IpPermissions = [{
                'IpProtocol':'TCP',
                'FromPort': 0,
                'ToPort': 65535,
                'IpRanges' : [{'CidrIp':'0.0.0.0/0'}],
                'Ipv6Ranges' : [{'CidrIpv6': '::/0'}]

            }]) 
        return security_group_id
        
    except ClientError as e:
        logging.error(e)

def instance_create():
    try:
        # ec2 = boto3.resource('ec2',region_name='ap-south-1')
        group_id = create_security_g()
        instance = ec2.create_instances(
            ImageId = 'ami-03cfb5e1fb4fac428',
            MinCount = 1,
            MaxCount = 1,
            InstanceType = 't2.micro',
            KeyName = 'Mumbaikey2020',
            # NetworkInterfaces=[{'SubnetId': subnet.id, 'DeviceIndex': 0, 'AssociatePublicIpAddress': True, 'Groups': [sec_group.group_id]}])
            SecurityGroupIds = [group_id])
        
   
        print(instance[0].id)
    except ClientError as e:
        logging.error(e)

def start_instace():
    try:    
        instances = ['i-025d689ec1a09f857','i-0de056058ec467381'] 
        for inst_id in instances: 
            ec2 = boto3.resource('ec2',region_name='ap-south-1')
            ec2.Instance(inst_id).start()
        
    except ClientError as e:
        logging.error(e)

def stop_instace():
    try:   
        instances = ['i-025d689ec1a09f857','i-0de056058ec467381'] 
        for inst_id in instances:
            ec2 = boto3.resource('ec2',region_name='ap-south-1')
            ec2.Instance(inst_id).stop()
                
    except ClientError as e:
        logging.error(e)


def terminate_instance():
    try:
        ec2 = boto3.resource('ec2',region_name='ap-south-1')
        ec2.Instance('i-0ed4ffe067eab17c1').terminate()
    except ClientError as e:
        logging.error(e)


# start_instace()
# stop_instace()
# print(create_security_g())
instance_create()
# terminate_instance()