#Question 4di TCP client server program
#Client program
#Create a socket server and client. The client sends “Hello from client!”,
#the server receives and prints it, and both programs include basic error handling
"""
  Communication sequence
  Step 1. The server creates a TCP socket, binds it to 127.0.0.1 and port 5000, and begins listening.
  Step 2. The client creates its TCP socket and connects to the same host and port.
  Step 3. The server accepts the connection and obtains a new connection socket.
  Step 4. The client encodes the text as bytes and sends it with sendall().
  Step 5. The server receives the bytes, decodes them to text and prints the message.
  Step 6. with blocks close all sockets automatically. OSError handles common network failures.

"""
# client.py
import socket

HOST = "127.0.0.1"
PORT = 5000
MESSAGE = "Hello from client!"

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(MESSAGE.encode("utf-8"))
        print("Message sent successfully.")
except OSError as error:
    print("Client network error:", error)


"""
   How to run the programs
   Step 1. Save the first program as server.py and the second as client.py.
   Step 2. Open two terminals. Run python server.py in the first terminal.
   Step 3. While the server is listening, run python client.py in the second terminal.
   Step 4. The server terminal displays the received message. If the client is started first, its connection attempt fails because no server is listening.
   Expected output
   server listening on 127.0.0.1:5000
   Connected by: (client address)
   Received: Hello from client!
"""