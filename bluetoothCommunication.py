import serial
import time

def send_command(command):
    port = '/dev/cu.usbmodem101'  # Use your specified port
    baud_rate = 9600  # Must match the baud rate set in your Arduino sketch

    try:
        # Open the serial port
        ser = serial.Serial(port, baud_rate, timeout=1)
        time.sleep(2)  # Wait for the Arduino to initialize

        # Send the command to the Arduino
        ser.write((command + '\n').encode())
        print(f"Sent command '{command}' to Arduino")

        # Optionally, read the response from the Arduino
        # response = ser.readline().decode().strip()
        # print(f"Arduino response: {response}")

        ser.close()
    except serial.SerialException as e:
        print(f"Error: {e}")
        print("Failed to connect to Arduino.")

def main():
    while True:
        command = input("Enter 'lock' or 'unlock' (or 'exit' to quit): ").strip().lower()
        if command == 'exit':
            print("Exiting program.")
            break
        elif command in ['lock', 'unlock']:
            send_command(command)
        else:
            print("Invalid command. Please enter 'lock' or 'unlock'.")

if __name__ == '__main__':
    main()
