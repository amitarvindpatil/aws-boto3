import boto3
import logging
import json
from time import time


def getDynamoConnection(constants):
    return boto3.resource('dynamodb', region_name=constants['aws']['region'])


def getChatUserById(constants, dynamodb, userId):
    table = dynamodb.Table(constants['tables']['chat_user_details'])

    result = table.get_item(
        Key={
            'user_id': userId
        }
    )

    return result


def createChatUser(constants, dynamodb, requestBody):
    table = dynamodb.Table(constants['tables']['chat_user_details'])

    timestamp = int(time() * 1000)

    response = table.put_item(
        Item={
            'user_id': str(requestBody['user_id']),
            'nickname': requestBody['user_name'],
            'access_token': requestBody['access_token'],
            'created_date': timestamp,
            'updated_date': timestamp
        }
    )

    return response


def updateChatUser(constants, connection, requestBody):
    table = connection.Table(constants['tables']['chat_user_details'])

    updateExpression = ''
    expressionAttributeValues = {}

    if requestBody['access_token'] != None and requestBody['access_token'] != '':
        updateExpression += 'access_token = :at,'
        expressionAttributeValues[":at"] = requestBody['access_token']

        updateExpression += 'updated_date = :ud,'
        expressionAttributeValues[":ud"] = int(time() * 1000)

        updateExpression = updateExpression[0:updateExpression.rindex(',')]

    response = table.put_item(
        Key={
            'user_id': requestBody['user_id']
        },
        UpdateExpression="set " + updateExpression,
        ExpressionAttributeValues=expressionAttributeValues,
        ReturnValues="UPDATED_NEW"
    )

    return response


def getChatChannelById(constants, connection, chatUserIds):

    table = connection.Table(constants['tables']['chat_channel_details'])

    results = table.get_item(
        Key={
            'chat_user_ids': chatUserIds
        }
    )

    return results


def createChatChannel(constants, connection, requestBody):
    table = connection.Table(constants['tables']['chat_channel_details'])

    response = table.put_item(
        Item={
            'chat_user_ids': requestBody['chat_user_ids'],
            'from_user_id': requestBody['from_user_id'],
            'to_user_id': requestBody['to_user_id'],
            'created_date': requestBody['sendBirdChannelDetails']['created_at'],
            'updated_date': requestBody['sendBirdChannelDetails']['created_at'],
            'channel_name': requestBody['sendBirdChannelDetails']['name'],
            'channel_url': requestBody['sendBirdChannelDetails']['channel_url'],
            'channel_custom_type': requestBody['sendBirdChannelDetails']['custom_type'],
            'channel_is_ephemeral': requestBody['sendBirdChannelDetails']['is_ephemeral'],
            'channel_member_count': requestBody['sendBirdChannelDetails']['member_count'],
            'channel_cover_url': requestBody['sendBirdChannelDetails']['cover_url'],
            'channel_max_length_message': requestBody['sendBirdChannelDetails']['max_length_message'],
            'channel_operators': requestBody['sendBirdChannelDetails']['operators'],
            'channel_freeze': requestBody['sendBirdChannelDetails']['freeze']
        }
    )

    return response
