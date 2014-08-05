# cloudwatch2graphite

This application will output graphite counters for a list of AWS CloudWatch metrics

All you need to do is:
    conf/metrics.json.sample into conf/metrics.json
    conf/aws.json.sample   info conf/aws.json  and set up accessKeyId,secretAccesKey and region.

You'll find here the [reference](http://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/CW_Support_For_AWS.html) to NameSpace,metrics,units and dimensions you'll want to refer to set up metric.json 

# Usage

typically,to test you should simple run:

    cloudwatch2graphite

to test with all options:

    cloudwatch2graphite [--region region_name] [--aws aws_file] [--metrics metrics_file] 

# Example output

    aws.dynamodb.rad_impressions.throttledrequests.updateitem.sum.count 28.0 1359407920
    aws.elb.radimp.requestcount.sum.count 933.0 1359407920
    aws.dynamodb.rad_impressions.consumedwritecapacityunits.sum.count 890.0 1359407920

# Sending to Graphite

typically,in a cron. 

    cloudwatch2graphite | nc host 2013

