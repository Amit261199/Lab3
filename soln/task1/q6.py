import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'

tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	itemkey={
	'publisher' : 'O\'Reilly Media',
	'title' : 'Git Pocket Guide'
	}
	itemval=[
	'pages', 268
	]
	
	attrname,val=itemval
	dynamodb.Table(table_name).update_item(
	Key=itemkey,
	UpdateExpression='SET #key = :val',
	ExpressionAttributeNames={
		'#key' : attrname
	},
	ExpressionAttributeValues={
		':val' : val
	}
	)
	
else:
	print("error! No such table found")
