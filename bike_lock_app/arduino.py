import serial
import time

# Function to initialize serial communication with the Arduino
def connect_to_arduino(port='/dev/ttyACM0', baudrate=9600, timeout=1):
    try:
        arduino = serial.Serial(port, baudrate=baudrate, timeout=timeout)
        time.sleep(2)  # Wait for the connection to initialize
        print("Connection established to Arduino on port", port)
        return arduino
    except serial.SerialException:
        print("Error: Could not connect to Arduino on port", port)
        return None

# Function to send a lock command to the Arduino
def send_lock_command(arduino):
    if arduino:
        arduino.write(b'lock\n')  # Send the 'lock' command
        response = arduino.readline().decode('utf-8').strip()  # Read the response from the Arduino
        print("Arduino Response:", response)

# Function to send an unlock command to the Arduino
def send_unlock_command(arduino):
    if arduino:
        arduino.write(b'unlock\n')  # Send the 'unlock' command
        response = arduino.readline().decode('utf-8').strip()  # Read the response from the Arduino
        print("Arduino Response:", response)

# Example usage
if __name__ == "__main__":
    arduino = connect_to_arduino(port='/dev/ttyACM0')  # Adjust the port based on your system

    if arduino:
        # Send a lock command
        send_lock_command(arduino)
        time.sleep(2)  # Wait for 2 seconds

        # Send an unlock command
        send_unlock_command(arduino)

        # Close the connection to the Arduino when done
        arduino.close()
