import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        telemetry = record['body']
        if telemetry['engine_temp_c'] > 120:
            # Send high-priority alert
            boto3.client('sns').publish(
                TopicArn='arn:aws:sns:region:id:vehicle-alerts',
                Message='High engine temp detected',
                Subject='ALERT: Engine Temperature'
            )