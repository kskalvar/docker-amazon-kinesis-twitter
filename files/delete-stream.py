# Simple script to create a kinesis stream
# create-stream.py

import boto3

client = boto3.client('kinesis')
client.delete_stream(StreamName = "twitter")
