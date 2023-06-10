import boto3
ec2=boto3.client('ec2')
terminate=ec2.terminate_instances(
        InstanceIds=['i-06401f2d6d6606156']
)