import boto3
ec2=boto3.client('ec2')
stop=ec2.stop_instances(
    InstanceIds=['i-06401f2d6d6606156']

)