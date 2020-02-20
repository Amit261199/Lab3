import boto3
from boto3.dynamodb.conditions import Attr
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	attrname,attrval=['pages',300]
	response=dynamodb.Table(table_name).scan(
	FilterExpression=Attr(attrname).gt(attrval),
	ProjectionExpression='title,pages',
	)
	for i in response['Items']:
		print(i)
	
else:
	print("error! No such table found")
