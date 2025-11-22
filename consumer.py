import boto3


QUEUE_URL = "https://sqs.eu-north-1.amazonaws.com/985124894153/MyQueue"

sqs = boto3.client(
    "sqs",
    region_name="eu-north-1",
    aws_access_key_id=".....",
    aws_secret_access_key=".....",
)

sqs.set_queue_attributes(
    QueueUrl=QUEUE_URL,
    Attributes={
        "VisibilityTimeout": "0"  # in seconds
    }
)

# Send a message
# sqs.send_message(QueueUrl=QUEUE_URL, MessageBody="Hello from Python")

if __name__ == '__main__':
    resp = sqs.receive_message(QueueUrl=QUEUE_URL, MaxNumberOfMessages=1, WaitTimeSeconds=5)

    if "Messages" in resp:
        msg = resp["Messages"][0]
        print("Received:", msg["Body"])
        sqs.delete_message(QueueUrl=QUEUE_URL, ReceiptHandle=msg["ReceiptHandle"])
    else:
        print("No messages available")


