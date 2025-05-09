# udp_server.py 
import socket 
import threading 
 
# Server configuration 
HOST = '127.0.0.1'  # Standard loopback interface address (localhost) 
PORT = 65433        # Port to listen on (non-privileged ports are > 1023) 
 
def main(): 
    print("[STARTING] UDP Server is starting...") 
     
    # Create a UDP socket 
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     
    # Bind the socket to the address and port 
    server.bind((HOST, PORT)) 
     
    print(f"[LISTENING] UDP Server is listening on {HOST}:{PORT}") 
     
    try: 
        while True: 
            # Receive data and address from client 
            data, addr = server.recvfrom(1024) 
             
            # Process incoming data 
            if data: 
                message = data.decode('utf-8') 
                print(f"[{addr}] {message}") 
                 
                # Send a response back to the client 
                response = f"Server received: {message}" 
                server.sendto(response.encode('utf-8'), addr) 
    except KeyboardInterrupt: 
        print("[SHUTDOWN] UDP Server is shutting down...") 
    finally: 
        server.close() 
 
if __name__ == "__main__": 
    main()