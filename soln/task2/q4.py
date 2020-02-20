import boto3
from boto3.dynamodb.conditions import Key
from boto3.dynamodb.conditions import Attr
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='WebAccessLog'
tables=[]
targetip='191.182.199.16'

for i in dynamodb.tables.all():
	tables.append(i.table_name)
	
if table_name in tables:
	response=dynamodb.Table(table_name).query(
	KeyConditionExpression=Key('ipaddr').eq(targetip)
	)
	dates={}
	for i in response['Items']:
		date=i['timestamp'].split(':')[0]
		if date not in dates.keys():
			dates[date]=[1,i['bytes']]
		else:
			dates[date][0]=dates[date][0]+1
			dates[date][1]=dates[date][1]+i['bytes']
	print(dates)
else:
	print("error! No such table found")
