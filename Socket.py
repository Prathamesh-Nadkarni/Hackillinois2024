import socket
import cv2
import numpy as np

# Network configuration
server_ip = "192.168.1.36"  # Replace with your RPi's IP address
server_port = 8000  # Port used for communication

# Create a socket and connect to the Raspberry Pi
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
except socket.error as e:
    print("Error connecting to server:", e)
    exit(1)

while True:
    # Receive data from the Raspberry Pi
    packet = client_socket.recv(4096)
    if not packet:
        break

    # Decode the data as a NumPy array
    try:
        frame = np.frombuffer(packet, dtype=np.uint8)
        frame = cv2.imdecode(frame, -1)
        if frame is None:
            print("Error: Unable to decode frame.")
            continue
        # Reshape frame if needed
        # frame = frame.reshape((height, width, channels))  # Add dimensions according to your image size
    except cv2.error as e:
        print("Error decoding frame:", e)
        continue  # Skip to the next iteration

    # Display the frame on your laptop
    cv2.imshow('Raspberry Pi Stream', frame)

    # Check for 'q' key press to exit
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

# Close the socket and window
client_socket.close()
cv2.destroyAllWindows()
