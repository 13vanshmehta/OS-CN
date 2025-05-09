import socket

# Create UDP socket
udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(('localhost', 12345))
print("UDP Server is listening...")

while True:
    data, addr = udp_server.recvfrom(1024)
    print(f"Received from {addr}: {data.decode()}")
    udp_server.sendto(data, addr)  # Echo back
