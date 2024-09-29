import boto3
import time
import bluetoothCommunication 
# Initialize boto3 client for SQS
sqs = boto3.client('sqs',
                   region_name='us-east-1',
                   aws_access_key_id='AKIAU7WW6RTINRBKTCDG',
                   aws_secret_access_key='Bj36TpX+82D4o3x/9dvtclgjGLQGrazUiRUpiZiB')

# Replace this with your SQS queue URL
queue_url = 'https://sqs.us-east-1.amazonaws.com/342974434512/lockitup-queue'

def poll_sqs_queue(queue_url):
    try:
        while True:
            # Poll the queue for messages
            response = sqs.receive_message(
                QueueUrl=queue_url,
                MaxNumberOfMessages=10,  # Adjust this as per your needs (1 to 10)
                WaitTimeSeconds=10        # Long polling to reduce the number of API requests
            )

            # Check if any messages were received
            if 'Messages' in response:
                for message in response['Messages']:
                    # Process the message
                    if message['Body'] == 'Unlock':
                        print("Received message: Unlock")
                        bluetoothCommunication.send_command('unlock')

                        
                    elif message['Body'] == 'Lock':
                        print("Received message: lock")
                        bluetoothCommunication.send_command('lock')
                    else:
                        print(f"Received message WRONG WRONG WRONG PLEASE SEND unlock OR lock: {message['Body']}")
    
                    # After processing the message, delete it from the queue
                    sqs.delete_message(
                        QueueUrl=queue_url,
                        ReceiptHandle=message['ReceiptHandle']
                    )
                    print(f"Deleted message: {message['MessageId']}")
            else:
                print("No messages found, waiting for new messages...")

            # Sleep for a while before polling again (optional)
            time.sleep(2)

    except Exception as e:
        print(f"Error polling SQS: {str(e)}")

if __name__ == "__main__":
    poll_sqs_queue(queue_url)
