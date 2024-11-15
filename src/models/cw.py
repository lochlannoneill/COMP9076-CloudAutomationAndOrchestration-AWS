import datetime
from src.utils.reading_from_user import read_nonnegative_integer, read_nonempty_string, read_nonnegative_float

class CWController:
    def __init__(self, client):
        """Initialize with a boto3 session."""
        self.client = client

    # TODO
    def list_metrics(self):
        """List all CloudWatch metrics."""
        response = self.client.list_metrics()
        for metric in response['Metrics']:
            print(f"Namespace: {metric['Namespace']}")
            print(f"Metric Name: {metric['MetricName']}")
            print(f"Dimensions: {metric['Dimensions']}")
            print()

    # TODO
    def get_metric_data(self):
        """Get metric data for a specified metric."""
        namespace = read_nonempty_string("Enter the Namespace: ")
        metric_name = read_nonempty_string("Enter the Metric Name: ")
        dimensions = read_nonempty_string("Enter the Dimensions (comma-separated key=value): ")
        dimensions = [d.split('=') for d in dimensions.split(',')]
        start_time = read_nonempty_string("Enter the Start Time (YYYY-MM-DD HH:MM:SS): ")
        end_time = read_nonempty_string("Enter the End Time (YYYY-MM-DD HH:MM:SS): ") #TODO - data validation
        period = read_nonnegative_integer("Enter the Period (in seconds): ")
        response = self.client.get_metric_data(
            MetricDataQueries=[
                {
                    'Id': 'm1',
                    'MetricStat': {
                        'Metric': {
                            'Namespace': namespace,
                            'MetricName': metric_name,
                            'Dimensions': [{d[0]: d[1]} for d in dimensions]
                        },
                        'Period': period,
                        'Stat': 'Average'
                    },
                    'ReturnData': True
                },
            ],
            StartTime=datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S"),
            EndTime=datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")
        )
        print(response)

    # TODO
    def put_metric_data(self):
        """Put metric data for a specified metric."""
        namespace = read_nonempty_string("Enter the Namespace: ")
        metric_name = read_nonempty_string("Enter the Metric Name: ")
        dimensions = read_nonempty_string("Enter the Dimensions (comma-separated key=value): ")
        dimensions = [d.split('=') for d in dimensions.split(',')]
        value = read_nonnegative_float("Enter the Value: ")
        timestamp = read_nonempty_string("Enter the Timestamp (YYYY-MM-DD HH:MM:SS): ")
        response = self.client.put_metric_data(
            Namespace=namespace,
            MetricData=[
                {
                    'MetricName': metric_name,
                    'Dimensions': [{d[0]: d[1]} for d in dimensions],
                    'Value': value,
                    'Timestamp': datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                },
            ]
        )
        print(response)

    # TODO
    def set_alarm(self):
        print("Not implemented yet.")

    # TODO
    def delete_alarm(self):
        print("Not implemented yet.")
    
    # TODO 
    def free_tier_aws_services(self):
        print("Not implemented yet.")