import boto3
import json

textract = boto3.client('textract')


def lambda_handler(event,context):
    print('Event Recieved:'+ json.dumps(event))
    
    
    response = textract.get_document_text_detection(
    JobId = event['JobId'],
    MaxResults=100,
    )
    print('The text identified is:'+ json.dumps(response))
