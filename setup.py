import boto3
import json


def batch_write(table_name, contents):
  table = dynamodb.Table(table_name)
  batch_start = 0
  lcontent = len(contents)
  while True:
    if batch_start > lcontent:
      break

    batch_contents = contents[batch_start:batch_start + 25]
    with table.batch_writer() as batch:
      for item in batch_contents:
        batch.put_item(Item=item)

    batch_start += 25

# Add Users Data in DB
def add_users():
  print("Adding Users...")
  fd = open("data/devhub/users.json", "r")
  fd_content = json.loads(fd.read())
  batch_write("Users", fd_content)
  fd.close()

# Add Repositories Data in DB
def add_repositories():
  print("Adding Repositories...")
  fd = open("data/devhub/repositories.json", "r")
  fd_content = json.loads(fd.read())
  batch_write("Repositories", fd_content)
  fd.close()

# Add Commits Data in DB
def add_commits():
  print("Adding Commits...")
  fd = open("data/devhub/commits.json", "r")
  fd_content = json.loads(fd.read())
  batch_write("Commits", fd_content)
  fd.close()

# Add Issues Data in DB
def add_issues():
  print("Adding Issues...")
  fd = open("data/devhub/issues.json", "r")
  fd_content = json.loads(fd.read())
  batch_write("Issues", fd_content)
  fd.close()

# Creates 'Users' Table in DB
def create_users():
  print("Creating 'Users' Table...")

  dynamodb.create_table(
    TableName='Users',
    KeySchema=[
      {
          'AttributeName': 'username',
          'KeyType': 'HASH'
      },
      {
          'AttributeName': 'email',
          'KeyType': 'RANGE'
      }
    ],
    AttributeDefinitions=[
      {
          'AttributeName': 'username',
          'AttributeType': 'S'
      },
      {
          'AttributeName': 'email',
          'AttributeType': 'S'
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 10,
      'WriteCapacityUnits': 10
    }
  )
  add_users()

# Creates 'Repositories' Table in DB
def create_repositories():
  print("Creating 'Repositories' Table...")
  dynamodb.create_table(
    TableName='Repositories',
    KeySchema=[
      {
          'AttributeName': 'name',
          'KeyType': 'HASH'
      },
      {
          'AttributeName': 'owner',
          'KeyType': 'RANGE'
      }
    ],
    AttributeDefinitions=[
      {
          'AttributeName': 'name',
          'AttributeType': 'S'
      },
      {
          'AttributeName': 'owner',
          'AttributeType': 'S'
      },
      {
          'AttributeName': 'id',
          'AttributeType': 'N'
      }
    ],
    GlobalSecondaryIndexes=[
      {
        'IndexName': 'id-index',
        'KeySchema': [
          {
            'KeyType': 'HASH',
            'AttributeName': 'id'
          }
        ],
        'Projection': {
          'ProjectionType': 'ALL'
        },
        'ProvisionedThroughput': {
          'ReadCapacityUnits': 10,
          'WriteCapacityUnits': 10
        }
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 10,
      'WriteCapacityUnits': 10
    }
  )
  add_repositories()

# Creates 'Issues' Table in DB
def create_issues():
  print("Creating 'Issues' Table...")
  dynamodb.create_table(
    TableName='Issues',
    KeySchema=[
      {
          'AttributeName': 'title',
          'KeyType': 'HASH'
      },
      {
          'AttributeName': 'repo_id',
          'KeyType': 'RANGE'
      }
    ],
    AttributeDefinitions=[
      {
          'AttributeName': 'title',
          'AttributeType': 'S'
      },
      {
          'AttributeName': 'repo_id',
          'AttributeType': 'N'
      },
      {
          'AttributeName': 'reporter',
          'AttributeType': 'S'
      }
    ],
    LocalSecondaryIndexes=[
      {
        'IndexName': 'reporter-index',
        'KeySchema': [
          {
            'KeyType': 'HASH',
            'AttributeName': 'title'
          },
          {
            'KeyType': 'RANGE',
            'AttributeName': 'reporter'
          }
        ],
        'Projection': {
          'ProjectionType': 'ALL'
        }
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 10,
      'WriteCapacityUnits': 10
    }
  )
  add_issues()

# Creates 'Commits' Table in DB
def create_commits():
  print("Creating 'Commits' Table...")
  dynamodb.create_table(
    TableName='Commits',
    KeySchema=[
      {
          'AttributeName': 'project_id',
          'KeyType': 'HASH'
      },
      {
          'AttributeName': 'sha',
          'KeyType': 'RANGE'
      }
    ],
    AttributeDefinitions=[
      {
          'AttributeName': 'project_id',
          'AttributeType': 'N'
      },
      {
          'AttributeName': 'sha',
          'AttributeType': 'S'
      }
    ],
    ProvisionedThroughput={
      'ReadCapacityUnits': 10,
      'WriteCapacityUnits': 10
    }
  )
  add_commits()

def init_setup():
  create_users()
  create_repositories()
  create_issues()
  create_commits()

if __name__ == "__main__":
  dynamodb = boto3.resource('dynamodb', region_name='ap-south-1', endpoint_url="http://localhost:8000")
  init_setup()
