# Simple script to create a kinesis stream
# create-stream.py

import boto3

client = boto3.client('kinesis')
client.create_stream(StreamName = "twitter", ShardCount = 1)
