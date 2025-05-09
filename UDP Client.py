import socket

# Create UDP socket
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = b'Hello, UDP Server!'
udp_client.sendto(message, ('localhost', 12345))

data, addr = udp_client.recvfrom(1024)
print(f"Received: {data.decode()}")

udp_client.close()
