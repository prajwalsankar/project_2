'''import paramiko

hostname = 'ip-172-31-35-124.ap-south-1.compute.internal'
myuser   = 'ec2-user'
mySSHK   = 'C:\\Users\\dell\\Downloads\\ec2keypair.ppk'
sshcon   = paramiko.SSHClient()  # will create the object
sshcon.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # no known_hosts error
sshcon.connect(hostname, username=myuser, key_filename=mySSHK) # no passwd needed
'''

import boto3

import botocore

import paramiko

key = paramiko.RSAKey.from_private_key_file("C:/Users/dell/Downloads/hi.pem")

client = paramiko.SSHClient()

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Connect/ssh to an instance

try:

    # Here 'ubuntu' is user name and 'instance_ip' is public IP of EC2

    client.connect(hostname=r'ip-172-31-35-124.ap-south-1.compute.internal', username="ec2-user", pkey=key,port=22)

    # Execute a command(cmd) after connecting/ssh to an instance

    stdin, stdout, stderr = client.exec_command('ls')

    print(stdout.read())

    # close the client connection once the job is done

    client.close()


except Exception as e:
    print(e)
