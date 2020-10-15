import boto3
# delete_table()
# delete_item()
# put_item()
# query()
# scan()
# get_item()
# update_item()
# list_tables()
# describe_table()
# batch_get_item()
# batch_write_item()


def create_table():
    dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
    response = dyndb_client.create_table(
        AttributeDefinitions=[
            {
                'AttributeName': 'user_id',
                'AttributeType': 'N'
            },
        ],
        TableName='users',
        KeySchema=[
            {
                'AttributeName': 'user_id',
                'KeyType': 'HASH'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 1,
            'WriteCapacityUnits': 1
        }
    )
    print("created_table", response)


def delete_table():
    dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
    response = dyndb_client.delete_table(
        TableName='users'
    )
    print("delete_table", response)


def delete_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.delete_item(
        Key={
            'user_id': 2
        })

    print("delete_item", response)


def put_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.put_item(
        Item={
            'user_id': 2,
            'user_name': 'Amit Patil',
            'age': 28,
            'status': True,
            'subject': ['Math', 'Marathi'],
            'data': {
                'math': '35',
                'bb': 'bb'
            },
            'year': [{
                'aa': 'aa',
                'cc': 'cc'
            }],
        })
    print("put_item", response)


def query():
    dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
    response = dyndb_client.query(
        TableName='string'
    )
    print("query", response)


def scan():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.scan()
    print("scan", response)


def get_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.get_item(
        Key={
            'user_id': 2
        })
    print("get_item", response)


def update_item():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')

    response = table.update_item(
        Key={
            'user_id': 2
        },
        UpdateExpression="set age=:age,phone=:ph",
        ExpressionAttributeValues={
            ':age': 30,
            ':ph': 98989898,
        },
        ReturnValues="UPDATED_NEW"

    )
    print("update_item", response)


def list_tables():
    dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
    response = dyndb_client.list_tables()
    print("list_tables", response)


def describe_table():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.Table('users')
    response = table.describe_table()
    print(" describe_table", response)

# def batch_get_item():
#     dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
#     response = dyndb_client.batch_get_item(
#         RequestItems={
#             'string': {
#                 'Keys': [
#                     {
#                         'string': {
#                             'S': 'string',
#                             'N': 'string',
#                             'B': b'bytes',
#                             'SS': [
#                                 'string',
#                             ],
#                             'NS': [
#                                 'string',
#                             ],
#                             'BS': [
#                                 b'bytes',
#                             ],
#                             'M': {
#                                 'string': {'... recursive ...'}
#                             },
#                             'L': [
#                                 {'... recursive ...'},
#                             ],
#                             'NULL': True|False,
#                             'BOOL': True|False
#                         }
#                     },
#                 ]
#     )
#     print("def describe_table",response)

# def batch_write_item():
#     dyndb_client = boto3.client('dynamodb', region_name='us-east-1')
#     response = dyndb_client.batch_write_item(
#     RequestItems={
#         'string': [
#             {
#                 'PutRequest': {
#                     'Item': {
#                         'string': {
#                             'S': 'string',
#                             'N': 'string',
#                             'B': b'bytes',
#                             'SS': [
#                                 'string',
#                             ],
#                             'NS': [
#                                 'string',
#                             ],
#                             'BS': [
#                                 b'bytes',
#                             ],
#                             'M': {
#                                 'string': {'... recursive ...'}
#                             },
#                             'L': [
#                                 {'... recursive ...'},
#                             ],
#                             'NULL': True|False,
#                             'BOOL': True|False
#                         }
#                     }
#                 },
#                 'DeleteRequest': {
#                     'Key': {
#                         'string': {
#                             'S': 'string',
#                             'N': 'string',
#                             'B': b'bytes',
#                             'SS': [
#                                 'string',
#                             ],
#                             'NS': [
#                                 'string',
#                             ],
#                             'BS': [
#                                 b'bytes',
#                             ],
#                             'M': {
#                                 'string': {'... recursive ...'}
#                             },
#                             'L': [
#                                 {'... recursive ...'},
#                             ],
#                             'NULL': True|False,
#                             'BOOL': True|False
#                         }
#                     }
#                 }
#             },
#         ]
#     }
#     print("def describe_table",response)


# create_table()
delete_table()
# put_items()
# get_item()
# list_tables()
# update_item()
# scan()
# describe_table() -------------------------
# delete_item()
