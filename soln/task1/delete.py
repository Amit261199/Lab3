import boto3
dynamodb=boto3.client("dynamodb",region_name='ap-south-1', endpoint_url="http://localhost:8000")

response=dynamodb.delete_table(TableName='Books')
