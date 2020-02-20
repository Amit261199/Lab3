import boto3
from boto3.dynamodb.conditions import Key
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	
	find_isbn='9781491904244'
	response=dynamodb.Table('Books').query(
	IndexName='isbn-index',
	Select='ALL_ATTRIBUTES',
	KeyConditionExpression=Key('isbn').eq(find_isbn)
	)

	print(str(len(response['Items']))+' book(s) found')
	print('-------------------------------')
	for i in response['Items']:
		print(i)
		print('-------------------------------')
	
else:
	print("error! No such table found")
