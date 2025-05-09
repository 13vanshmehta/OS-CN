import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client_socket.connect(('localhost', 12345))

# Send message
client_socket.sendall(b'Hello, TCP Server!')

# Receive response
data = client_socket.recv(1024)
print(f"Received: {data.decode()}")

client_socket.close()
