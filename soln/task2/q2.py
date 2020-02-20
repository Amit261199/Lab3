import boto3
import json
dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")

table_name='WebAccessLog'
tables=[]
batch_size=25
for i in dynamodb.tables.all():
	tables.append(i.table_name)
	
if table_name in tables:
	f=open('../../data/logs/web_access_log.json')
	data=json.load(f)
	size=len(data)
	i=0;
	f.close()
	while i<size:
		with dynamodb.Table(table_name).batch_writer() as batch:
			for item in data[i:min(i+batch_size,size)]:
				batch.put_item(Item=item)
		i=i+batch_size
	print('Table '+table_name+' has '+str(dynamodb.Table(table_name).item_count)+' items')
else:
	print("error! No such table found")
