import boto3,json,os

textract = boto3.client('textract')
lambda_my = boto3.client('lambda')

def lambda_handler(event, context):
    print('Event Recieved:'+ json.dumps(event))
    
    source_bucket =event['Records'][0]['s3']['bucket']['name']
    source_object =event['Records'][0]['s3']['object']['key']
    response = textract.start_document_text_detection(
        DocumentLocation={
            'S3Object':{
                'Bucket': source_bucket,
                'Name': source_object
            }
        },
        NotificationChannel={
        'SNSTopicArn': 'arn:aws:sns:us-east-1:243987456759:textracttopic',
        'RoleArn': 'arn:aws:iam::243987456759:role/TextracttoSNS'
    },
        OutputConfig={
            'S3Bucket':'imagesbucketdivya'

        }
       )
    lambda_response = lambda_my.invoke(
                FunctionName = 'textraxt2',
                InvocationType = 'Event',
                Payload = json.dumps(response)
                )
    print(response)