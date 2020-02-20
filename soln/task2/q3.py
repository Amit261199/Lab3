import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='WebAccessLog'
tables=[]
targetip='188.45.108.168'
targetattr='status'
targetattrval=200
for i in dynamodb.tables.all():
	tables.append(i.table_name)
	
if table_name in tables:
	response=dynamodb.Table(table_name).query(
	KeyConditionExpression=Key('ipaddr').eq(targetip),
	FilterExpression=Attr(targetattr).ne(targetattrval)
	)
	print(len(response['Items']))
else:
	print("error! No such table found")
