import argparse
from .version import __version__

def main():
    parser = argparse.ArgumentParser(description="cloudwatch2graphite will output graphite counters for a list of AWS Cloudwatch metrics")
    parser.add_argument('--version', action='version', version='%(prog)s '+__VERSION__)
    parser.add_argument("--region",required=True)
    parser.add_argument("--aws",required=True)
    parser.add_argument("--metrics",required=True)

    args = parser.parse_args()



      
