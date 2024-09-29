import boto3
import json

# Initialize boto3 client for SQS
sqs = boto3.client('sqs',
                   region_name='us-east-1',
                   aws_access_key_id='AKIAU7WW6RTINRBKTCDG',
                   aws_secret_access_key='Bj36TpX+82D4o3x/9dvtclgjGLQGrazUiRUpiZiB')

# Replace this with your SQS queue URL
Queue_url = 'https://sqs.us-east-1.amazonaws.com/342974434512/lockitup-queue'
# Optional: Specify message body
message_body = {
"open"
}

def create_queue(Queue_url):
    """
    Creates an SQS queue with the given name if it doesn't exist.
    """
    try:
        response = sqs.create_queue(QueueUrl=Queue_url)
        queue_url = response['QueueUrl']
        print(f"Queue {Queue_url} created or exists: {queue_url}")
        return queue_url
    except Exception as e:
        print(f"Error creating queue: {str(e)}")
        return None

def send_message(queue_url, message_body):
    """
    Sends a message to the specified SQS queue.
    """
    try:
        # Send a message to the queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)  # Convert the message to JSON string
        )
        print(f"Message sent! Message ID: {response['MessageId']}")
    except Exception as e:
        print(f"Error sending message: {str(e)}")

if __name__ == "__main__":
    # Step 1: Create the queue (if it doesn't exist) and get its URL
    queue_url = create_queue(Queue_url)
    
    if queue_url:
        # Step 2: Send the message to the queue
        send_message(queue_url, message_body)
