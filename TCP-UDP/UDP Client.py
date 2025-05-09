# udp_client.py 
import socket 
import sys 
 
# Client configuration 
HOST = '127.0.0.1'  # The server's hostname or IP address 
PORT = 65433        # The port used by the server 
 
def main(): 
    # Create a UDP socket 
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
     
    try: 
        print(f"[READY] UDP Client ready to send messages to {HOST}:{PORT}") 
         
        while True: 
            # Get input from the user 
            message = input("Enter message (or 'quit' to exit): ") 
             
            # Check if the user wants to quit 
            if message.lower() == 'quit': 
                break 
                 
            # Send the message to the server 
            client.sendto(message.encode('utf-8'), (HOST, PORT)) 
             
            # Set a timeout for receiving a response 
            client.settimeout(5.0) 
             
            try: 
                # Try to receive a response from the server 
                data, server = client.recvfrom(1024) 
                response = data.decode('utf-8') 
                print(f"[SERVER] {response}") 
            except socket.timeout: 
                print("[TIMEOUT] No response received from server.") 
             
    except Exception as e: 
        print(f"[ERROR] {e}") 
    finally: 
        # Close the socket 
        client.close() 
        print("[CLOSED] Client socket closed.") 
 
if __name__ == "__main__": 
    main()