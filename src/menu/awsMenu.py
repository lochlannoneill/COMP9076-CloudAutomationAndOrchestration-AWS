from src.utils.reading_from_user import read_range_integer
from src.menu.ec2Menu import ec2Menu
from src.menu.volumeMenu import volumeMenu
from src.models.volumes import volumes
from src.models.ec2 import EC2Controller

class awsMenu:
    def __init__(self):
        self.ec2_menu = ec2Menu()
        self.volume_menu = volumeMenu()
        self.options = {
            "EC2 Instances": 1,
            "EBS Volumes": 2,
            "S3 Buckets": 3,
            "Monitoring": 4,
            "Back": 5
        }

    def _display(self):
        print("\nAWS Main Menu")
        for option, number in self.options.items():
            print(f"{number}. {option}")

    def handle(self, aws_resource):
        while True:
            self._display()
            choice = read_range_integer(
                "Select from menu: ",
                min(self.options.values()),
                max(self.options.values())
            )
            
            # EC2 Instances
            if choice == self.options["EC2 Instances"]:
                ec2_controller = EC2Controller(
                    aws_resource.get_ec2_resource(),
                    aws_resource._create_client("ec2")
                )
                self.ec2_menu.handle(ec2_controller)
                
            # EBS Volumes
            if choice == self.options["EBS Volumes"]:
                vol = volumes(aws_resource._create_client("ec2"))
                self.volume_menu.handle(vol)
                
            # S3 Buckets
            if choice == self.options["S3 Buckets"]:
                pass  # TODO
            
            # Monitoring
            if choice == self.options["Monitoring"]:
                pass  # TODO
            
            # Back
            if choice == self.options["Back"]:
                return False
