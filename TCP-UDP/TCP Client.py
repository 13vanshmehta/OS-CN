# tcp_client.py 
import socket 
import sys 
 
# Client configuration 
HOST = '127.0.0.1'  # The server's hostname or IP address 
PORT = 65432        # The port used by the server 
 
def main(): 
    # Create a TCP socket 
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
     
    try: 
        # Connect to the server 
        print(f"[CONNECTING] Connecting to server at {HOST}:{PORT}...") 
        client.connect((HOST, PORT)) 
        print("[CONNECTED] Connected to server.") 
         
        while True: 
            # Get input from the user 
            message = input("Enter message (or 'quit' to exit): ") 
             
            # Check if the user wants to quit 
            if message.lower() == 'quit': 
                break 
                 
            # Send the message to the server 
            client.sendall(message.encode('utf-8')) 
             
            # Receive the response from the server 
            data = client.recv(1024) 
            response = data.decode('utf-8') 
            print(f"[SERVER] {response}") 
             
    except ConnectionRefusedError: 
        print("[ERROR] Connection refused. Make sure the server is running.") 
    except Exception as e: 
        print(f"[ERROR] {e}") 
    finally: 
        # Close the connection 
        client.close() 
        print("[DISCONNECTED] Disconnected from the server.") 
 
if __name__ == "__main__": 
    main() 