import argparse
import os
import json
from version import __version__
from fetcher import fetcher

def main():
    parser = argparse.ArgumentParser(description="cloudwatch2graphite will output graphite counters for a list of AWS Cloudwatch metrics")
    parser.add_argument('--version', action='version', version='%(prog)s '+__version__)
    parser.add_argument("--region",required=False)
    parser.add_argument("--aws",required=True)
    parser.add_argument("--metrics",required=True)

    args = parser.parse_args()
    if not os.path.exists(args.aws) or not os.path.exists(args.metrics):
        print "aws file or metrics file not found"
        return 

    config = {}
    with open(args.aws) as f:
        config['aws'] = json.loads(f.read())
    with open(args.metrics) as f:
        config['metrics'] = json.loads(f.read())

    if args.region:
        config['aws']['region'] = args.region

    fetcher(config)

    return

if __name__ == '__main__':
    main()
