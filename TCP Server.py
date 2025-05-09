import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to address and port
server_socket.bind(('localhost', 12345))

# Listen for connections
server_socket.listen(1)
print("Server is listening on 12345...")

# Accept a connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    data = conn.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    conn.sendall(data)  # Echo back
server_socket.close()