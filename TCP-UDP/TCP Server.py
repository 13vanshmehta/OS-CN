# tcp_server.py 
import socket 
import threading 
 
# Server configuration 
HOST = '127.0.0.1'  # Standard loopback interface address (localhost) 
PORT = 65432        # Port to listen on (non-privileged ports are > 1023) 
 
def handle_client(conn, addr): 
    """Handle individual client connections""" 
    print(f"[NEW CONNECTION] {addr} connected.") 
     
    try: 
        connected = True 
        while connected: 
            # Receive data from the client (buffer size of 1024 bytes) 
            data = conn.recv(1024) 
            if not data: 
                # If no data is received, the client has disconnected 
                break 
                 
            # Decode and print the received message 
            message = data.decode('utf-8') 
            print(f"[{addr}] {message}") 
             
            # Process the message (in this example, we just echo it back) 
            response = f"Server received: {message}" 
            conn.sendall(response.encode('utf-8')) 
    except Exception as e: 
        print(f"[ERROR] {e}") 
    finally: 
        # Close the connection 
        conn.close() 
        print(f"[DISCONNECTED] {addr} disconnected.") 
 
def main(): 
    print("[STARTING] Server is starting...") 
     
    # Create a TCP socket 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
     
    # Bind the socket to the address and port 
    server.bind((HOST, PORT)) 
     
    # Listen for incoming connections (5 is the backlog parameter) 
    server.listen(5) 
    print(f"[LISTENING] Server is listening on {HOST}:{PORT}") 
     
    try: 
        while True: 
            # Accept a connection 
            conn, addr = server.accept() 
             
            # Create a new thread to handle the client 
            thread = threading.Thread(target=handle_client, args=(conn, addr)) 
            thread.daemon = True 
            thread.start() 
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}") 
    except KeyboardInterrupt: 
        print("[SHUTDOWN] Server is shutting down...") 
    finally: 
        server.close() 
 
if __name__ == "__main__": 
    main()