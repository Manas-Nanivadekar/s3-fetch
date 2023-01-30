import sys
import boto3

s3 = boto3.resource('s3')
s3.download_file(sys.argv[1], sys.argv[2], sys.argv[3])
# sys.argv[1] = bucket name
# sys.argv[2] = file name
# sys.argv[3] = local file name
