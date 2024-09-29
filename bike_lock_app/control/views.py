from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
import serial
import threading
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
from django.views.decorators.csrf import csrf_exempt 


# Create your views here.
# control/views.py
from django.contrib.auth.decorators import login_required

def insert_number_view(request):
    return render(request, 'control/insert_number.html')

@login_required
def home(request):
    return render(request, 'control/home.html')

def loginPage(request):
    return render(request, 'control/loginPage.html')

def lockPage(request):
    return render(request, 'control/lockPage.html')

# Initialize serial connection (adjust 'COM3' or '/dev/ttyUSB0' and baudrate as needed)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
except serial.SerialException:
    ser = None  # Handle appropriately

lock = threading.Lock()

sqs = boto3.client('sqs', region_name='us-east-1')  # Set the appropriate AWS region

# Replace with your SQS queue URL
queue_url = 'https://sqs.us-east-1.amazonaws.com/342974434512/lockitup-queue'

def send_message_to_sqs(message_body):
    try:
        # Send a message to the specified SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )

        # Print the response details
        print(f"Message ID: {response['MessageId']}")
        print(f"MD5 of Body: {response['MD5OfMessageBody']}")
        return response

    except (NoCredentialsError, PartialCredentialsError) as e:
        print(f"Credentials error: {e}")
        return None

@api_view(['POST'])
@csrf_exempt
def lock_bike(request):
    send_message_to_sqs("Lock")
    return JsonResponse({'status': 'locked'})  # Directly respond without checking request.method

@api_view(['POST'])
@csrf_exempt
def unlock_bike(request):
    send_message_to_sqs("Unlock")
    return JsonResponse({'status': 'unlocked'})  # Directly respond without checking request.method


