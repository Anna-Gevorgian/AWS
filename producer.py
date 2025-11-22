import boto3


sqs = boto3.client(
    "sqs",
    region_name="eu-north-1",
    aws_access_key_id=".....",
    aws_secret_access_key=".....",
)


queue_url = "https://sqs.eu-north-1.amazonaws.com/985124894153/MyQueue"

if __name__ == '__main__':
    response = sqs.send_message(
        QueueUrl=queue_url,
        MessageBody='Hello from Python!'
    )

    print("Message ID:", response['MessageId'])


