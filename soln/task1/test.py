import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	
	find={
		'publisher': 'O\'Reilly Media',
		'title' : 'Git Pocket Guide'
	}
	response=dynamodb.Table('Books').get_item(
	Key=find
	)
	
	if 'Item' in response.keys():
		print('book found')
		print('-------------------------------')
		print(response['Item'])
	else:
		print('book not found')
	
else:
	print("error! No such table found")
