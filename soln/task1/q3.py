import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	f=open('../../data/books/books.json')
	Books=json.load(f)['books'][1:]
	f.close()
	with dynamodb.Table(table_name).batch_writer() as batch:
		for book in Books:
			batch.put_item(Item=book)
	print('table has '+ str(dynamodb.Table('Books').item_count) +' items')
	
else:
	print("error! No such table found")
