import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='WebAccessLog'
tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
	
if table_name in tables:
	print('Table '+table_name+' already exists')
else:
	response=dynamodb.create_table(
	TableName=table_name,
	AttributeDefinitions=[{
		'AttributeName' :'ipaddr',
		'AttributeType' : 'S'
	},
	{
		'AttributeName' :'req_no',
		'AttributeType' : 'N'
	}
	],
	KeySchema=[{
		'AttributeName' : 'ipaddr',
		'KeyType' : 'HASH'
	},
	{
		'AttributeName' : 'req_no',
		'KeyType' : 'RANGE'
	}	
	],
	ProvisionedThroughput=
	{
		'ReadCapacityUnits' : 10,
		'WriteCapacityUnits': 10
	}
	)
	print('Table '+table_name+' is in '+response.table_status+' state')
