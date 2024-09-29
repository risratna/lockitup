from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import JsonResponse
import serial
import threading

# Create your views here.
# control/views.py
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'control/home.html')


# Initialize serial connection (adjust 'COM3' or '/dev/ttyUSB0' and baudrate as needed)
try:
    ser = serial.Serial('COM3', 9600, timeout=1)
except serial.SerialException:
    ser = None  # Handle appropriately

lock = threading.Lock()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def lock_bike(request):
    print("Trying to lock")
    if request.method == 'POST':
        return JsonResponse({'status': 'locked'})  # Send a JSON response
    return JsonResponse({'error': 'Invalid request'}, status=400)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlock_bike(request):    
    print("Trying to unlock")
    if request.method == 'POST':
        # Code to send signal to Arduino for unlocking (replace with your actual logic)
        # send_signal_to_arduino('unlock')
        return JsonResponse({'status': 'unlocked'})  # Send a JSON response
    return JsonResponse({'error': 'Invalid request'}, status=400)

