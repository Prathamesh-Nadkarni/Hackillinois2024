from src import camera as camera_module
import time
import socket
import io

# Network configuration
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 8000))  # Replace with desired IP and port
server_socket.listen(0)

# Accept client connection
client_socket, address = server_socket.accept()
print(f"Connected to client: {address}")

if __name__ == '__main__':
    total_seconds = 60
    sample_hz = 10

    camera = camera_module.Camera({
        "show_preview": False
    })

    try:
        while True:
            camera.capture()
            image_bytes = camera.image_array.tobytes()
            client_socket.sendall(image_bytes)

            time.sleep(max(0, 1/sample_hz - (time.time() - start_time)))
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        # Cleanup
        client_socket.close()
        server_socket.close()
        if camera.cam:
            camera.cam.stop()
