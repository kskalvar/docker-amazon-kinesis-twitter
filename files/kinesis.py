# Example to use twitter api and feed data into kinesis

from TwitterAPI import TwitterAPI
import boto3
import json
import os

## twitter credentials
consumer_key = os.environ['CONSUMERKEY']
consumer_secret = os.environ['CONSUMERSECRET']
access_token_key = os.environ['ACCESSTOKEN']
access_token_secret = os.environ['ACCESSTOKENSEC']

api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

kinesis = boto3.client('kinesis')

request = api.request('statuses/filter', {'locations':'-90,-90,90,90'})
for item in request:
   kinesis.put_record(StreamName="twitter", Data=json.dumps(item), PartitionKey="filler")
