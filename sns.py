# create,list,delete,subscribe,unsub topic
import boto3

def create_topic():
    sns = boto3.client('sns', region_name='us-east-1')
    
    response = sns.create_topic(
        Name='hello-sns'
    )
    print("create_topic",response)

def list_topics():
    sns = boto3.client('sns', region_name='us-east-1')

    response = sns.list_topics()
    print("list_topic",response)

def delete_topic():
    sns = boto3.client('sns', region_name='us-east-1')

    response = sns.delete_topic(
        TopicArn='arn:aws:sns:us-east-1:020027843329:hello-sns'
    )
    print("delete_topic",response)
     

def subscribe():
    sns = boto3.client('sns', region_name='us-east-1')
    response = sns.subscribe(
        TopicArn='arn:aws:sns:us-east-1:020027843329:hello-sns',
        Protocol='sms',
        Endpoint='+919511785821'
    )
    print("subscribe_topic",response) 

def unsubscribe():
    sns = boto3.client('sns', region_name='us-east-1')
    response = sns.unsubscribe(
       SubscriptionArn='arn:aws:sns:us-east-1:020027843329:hello-sns'
    )
    print("Unsubscribe_topic",response) 

def publish():
    sns = boto3.client('sns', region_name='us-east-1')
    response = sns.publish(
        TopicArn='arn:aws:sns:us-east-1:020027843329:hello-sns',
        Message='This is amit',
        Subject='Information'
    )
    print("publish",response) 



# create_topic()
# list_topics()
# subscribe()
# publish()
# unsubscribe()
delete_topic()