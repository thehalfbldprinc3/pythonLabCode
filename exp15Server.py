import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
HOST = '127.0.0.1'  # Localhost
PORT = 12345
server_socket.bind((HOST, PORT))

# Start listening for connections
server_socket.listen()

print(f"Server is listening on {HOST}:{PORT}")

# Accept a connection
client_socket, addr = server_socket.accept()
print(f"Connected by {addr}")

# Receive data from the client
data = client_socket.recv(1024).decode('utf-8')
print(f"Received: {data}")

# Send a response
response = "Hello from the server!"
client_socket.send(response.encode('utf-8'))

# Close the connection
client_socket.close()
server_socket.close()