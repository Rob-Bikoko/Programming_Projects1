# This is the Server Program
import socket

HOST = '127.0.0.1' # Localhost
PORT = 65432 # Port to listen on

try:
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        print(f"Server listening on {HOST}:{PORT}")

        conn, addr = server_socket.accept()

        with conn:
            print(f"Connected by {addr}")

            data = conn.recv(1024)

            if data:
                print("Message received:", data.decode('utf-8'))
            else:
                print("No data received.")

except socket.error as e:
    print(f"Network error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

