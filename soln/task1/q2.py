import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	f=open('../../data/books/books.json')
	FirstBook=json.load(f)['books'][0]
	response=dynamodb.Table('Books').put_item(
	Item=FirstBook
	)
	f.close()
	#print(response)
	print('table has '+ str(dynamodb.Table('Books').item_count) +' items')
	
else:
	print("error! No such table found")
