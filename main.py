import sys
import boto3

s3 = boto3.resource('s3')
s3.download_file(sys.argv[1], sys.argv[2], sys.argv[3])
