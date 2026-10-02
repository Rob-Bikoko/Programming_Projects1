#Q3ii. Write a simple client-server program using Python's socket module.
#The client should connect to the server and send the message "Hello from client!".
#The server should receive the message and print it to the console. Include basic
#error handling for network operations.
# This is the ClientProgram
import socket

HOST = '127.0.0.1' # Server address
PORT = 65432 # Server port

try:
    # Create a TCP socket
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((HOST, PORT))

        message = "Hello from client!"
        client_socket.sendall(message.encode('utf-8'))

        print("Message sent successfully.")

except ConnectionRefusedError:
    print("Connection failed: Server is not running.")

except socket.error as e:
    print(f"Network error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")

