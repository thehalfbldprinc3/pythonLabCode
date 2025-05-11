import socket

# Create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
HOST = '127.0.0.1'
PORT = 12345
client_socket.connect((HOST, PORT))

# Send a message
message = "Hello from the client!"
client_socket.send(message.encode('utf-8'))

# Receive a response
response = client_socket.recv(1024).decode('utf-8')
print(f"Server Response: {response}")

# Close the connection
client_socket.close()