import boto3


dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
client = boto3.client('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
tables = client.list_tables()['TableNames']

if "Users" in tables:
  dynamodb.Table("Users").delete()

if "Repositories" in tables:
  dynamodb.Table("Repositories").delete()

if "Commits" in tables:
  dynamodb.Table("Commits").delete()

if "Issues" in tables:
  dynamodb.Table("Issues").delete()

if "Books" in tables:
  dynamodb.Table("Books").delete()

if "WebAccessLog" in tables:
  dynamodb.Table("WebAccessLog").delete()


