import socket

HOST = '127.0.0.1'
PORT = 8000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Listening on http://{HOST}:{PORT}/callback ...")

client_socket, addr = server_socket.accept()
request = client_socket.recv(1024).decode('utf-8')

print(f"Connected by {addr}")
print("Request received:")
print(request)

# Extract the authorization code from the request
if "GET /callback?" in request:
    # Grab the full query string
    request_line = request.split('\n')[0]
    query_string = request_line.split(' ')[1]  # e.g. /callback?code=AQDw...
    print("Query string:", query_string)

    # Send a basic HTML response
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html\r\n\r\n"
        "<html><body><h1>Authorization complete. You may close this window.</h1></body></html>"
    )
    client_socket.sendall(response.encode('utf-8'))

client_socket.close()
server_socket.close()