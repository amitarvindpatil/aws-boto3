import boto3

# Create SQS client


# create


def create_queue():

    sqs = boto3.client('sqs', region_name='us-east-1')
    response = sqs.create_queue(
        QueueName='SQS_QUEUE_NAME',
        Attributes={
            'DelaySeconds': '60',
            'MessageRetentionPeriod': '86400'
        }
    )

# list


def list_queues():
    # List SQS queues
    sqs = boto3.client('sqs', region_name='us-east-1')
    response = sqs.list_queues()

    print(response['QueueUrls'])


def get_queue_url():

    sqs = boto3.client('sqs', region_name='us-east-1')
    response = sqs.get_queue_url(QueueName='SQS_QUEUE_NAME')
    print(response['QueueUrl'])


# Delete SQS queue
def delete_queue():

    sqs = boto3.client('sqs', region_name='us-east-1')
    sqs.delete_queue(QueueUrl='SQS_QUEUE_URL')


def send_message():

    sqs = boto3.client('sqs', region_name='us-east-1')
    queue_url = 'https://queue.amazonaws.com/020027843329/SQS_QUEUE_NAME'

    # Send message to SQS queue
    response = sqs.send_message(
        QueueUrl=queue_url,
        DelaySeconds=10,
        MessageAttributes={
            'Title': {
                'DataType': 'String',
                'StringValue': 'The Whistler'
            }
        },
        MessageBody=('{\"name\":\"amit\"}')
    )

    print(response['MessageId'])


def receive_message():

    sqs = boto3.client('sqs', region_name='us-east-1')

    queue_url = 'https://queue.amazonaws.com/020027843329/SQS_QUEUE_NAME'

    # Receive message from SQS queue
    response = sqs.receive_message(
        QueueUrl=queue_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        VisibilityTimeout=0,
        WaitTimeSeconds=0
    )

    message = response['Messages'][0]
    message_body = message['Body']
    receipt_handle = message['ReceiptHandle']
    print(receipt_handle)


def delete_message():

    sqs = boto3.client('sqs', region_name='us-east-1')

    queue_url = 'https://queue.amazonaws.com/020027843329/SQS_QUEUE_NAME'
    sqs.delete_message(
        QueueUrl=queue_url,
        ReceiptHandle=''
    )
    print('Received and deleted message: %s' % message)


# list_queues()
# send_message()
# receive_message()
delete_message()
