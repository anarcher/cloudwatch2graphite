import boto
import boto.ec2.cloudwatch
import arrow

def fetcher(config):
    aws = config['aws']
    aws_access_key_id = aws['aws_access_key_id']
    aws_secret_access_key = aws['aws_secret_access_key']
    region = aws['region']

    c = boto.ec2.cloudwatch.connect_to_region(region,
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key)

    metrics = config['metrics']['metrics']

    for metric in metrics:
        metric_result = fetch_metric(c,metric)
        print(metric_result)

def fetch_metric(conn,metric_config):
    period = 60

    interval = 11
    utc_now = arrow.utcnow()
    start_time = utc_now.replace(minutes=-interval).datetime
    end_time = utc_now.datetime

    metric_name = metric_config["MetricName"]
    namespace = metric_config["Namespace"]
    statistics = metric_config["Statistics"]
    dimensions = metric_config["Dimensions"]
    unit = metric_config["Unit"]

    kwargs = {
        "period" :period,
        "start_time" : start_time,
        "end_time" : end_time,
        "metric_name" : metric_name,
        "namespace" : namespace,
        "statistics" : statistics,
        "dimensions" : dimensions,
        "unit" : unit,
    }
    result = conn.get_metric_statistics(**kwargs)
    return result




