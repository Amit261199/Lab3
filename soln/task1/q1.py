import boto3
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='Books'
tables=[]
for i in dynamodb.tables.all():
	tables.append(i.table_name)
if table_name in tables:
	print('Table '+table_name+' already exists')
else:
	response=dynamodb.create_table(
	TableName=table_name,
	AttributeDefinitions=[
		{'AttributeName': 'publisher',
		'AttributeType': 'S'},
		
		{'AttributeName': 'title',
		'AttributeType': 'S'},
		
		{'AttributeName': 'isbn',
		'AttributeType': 'S'}
		
	],
	
	KeySchema=[
	{'AttributeName': 'publisher',
		'KeyType': 'HASH'},
		
		{'AttributeName': 'title',
		'KeyType': 'RANGE'}
	],
	
	GlobalSecondaryIndexes=[
	
		{
			'IndexName' : 'isbn-index',
			'KeySchema' : [
			{'AttributeName': 'isbn',
				'KeyType': 'HASH'},
		
			],
			'Projection' : {'ProjectionType' : 'ALL'},
			'ProvisionedThroughput':
			{
				'ReadCapacityUnits' : 10,
				'WriteCapacityUnits' : 10
			}
		}
			
	],
	ProvisionedThroughput=
			{
				'ReadCapacityUnits' : 10,
				'WriteCapacityUnits' : 10
			}
	)
	
	print('Table '+table_name+' is in '+response.table_status+' state')
