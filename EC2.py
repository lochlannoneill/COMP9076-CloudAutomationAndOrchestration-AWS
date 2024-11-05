import boto3

class EC2Manager:
    def __init__(self, session):
        """Initialize with a boto3 session."""
        self.ec2 = session.client('ec2')

    def list_instances(self):
        """List all EC2 instances, grouped by running and stopped."""
        response = self.ec2.describe_instances()
        running_instances = []
        stopped_instances = []
        
        # Parse instances
        for reservation in response['Reservations']:
            for instance in reservation['Instances']:
                instance_info = {
                    "Instance ID": instance['InstanceId'],
                    "State": instance['State']['Name'],
                    "Type": instance['InstanceType'],
                    "Region": instance['Placement']['AvailabilityZone'],
                    "Launch Time": instance['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
                }
                if instance['State']['Name'] == 'running':
                    running_instances.append(instance_info)
                else:
                    stopped_instances.append(instance_info)
        
        print("\nRunning Instances:")
        for inst in running_instances:
            print(inst)
        
        print("\nStopped Instances:")
        for inst in stopped_instances:
            print(inst)

    def start_instance(self):
        """Start a specified EC2 instance."""
        instance_id = input("Enter the Instance ID to start: ")
        self.ec2.start_instances(InstanceIds=[instance_id])
        print(f"Starting instance {instance_id}...")

    def stop_instance(self):
        """Stop a specified EC2 instance."""
        instance_id = input("Enter the Instance ID to stop: ")
        self.ec2.stop_instances(InstanceIds=[instance_id])
        print(f"Stopping instance {instance_id}...")

    def create_ami(self):
        """Create an AMI from a specified EC2 instance."""
        instance_id = input("Enter the Instance ID to create AMI from: ")
        ami_name = input("Enter a name for the AMI: ")
        response = self.ec2.create_image(InstanceId=instance_id, Name=ami_name)
        print(f"AMI created: {response['ImageId']}")

    def delete_ami(self):
        """Delete a specified AMI."""
        ami_id = input("Enter the AMI ID to delete: ")
        self.ec2.deregister_image(ImageId=ami_id)
        print(f"Deleted AMI: {ami_id}")