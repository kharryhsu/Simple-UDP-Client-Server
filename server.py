import socket
import argparse

def start_server(addr='localhost', port=12345):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server_socket.bind((addr, port))
        
        print(f'Server is listening on port {addr}:{port}...')
        
        while True:
            try:
                data, client_address = server_socket.recvfrom(1024)
                
                print(f'Received from client {client_address}: {data.decode("utf-8")}')
                
                msg = input("Server: Enter message to send (or type 'exit' to end communication)\n> ")
                
                if msg.lower() == 'exit':
                    print("Ending connection with client.")
                    break
                
                try:
                    server_socket.sendto(msg.encode('utf-8'), client_address)
                except Exception as e:
                    print(f"Error sending message: {e}")
                    break
            except KeyboardInterrupt:
                print("Exited by user.")
            except Exception as e:
                print(f'Error handling client {client_address}: {e}')
    except KeyboardInterrupt:
        print("Exited by user.")
    except Exception as e:
        print(f'Server error: {e}')
    finally:
        server_socket.close()
        print("Server shutdown.")

def parse_arguments():
    parser = argparse.ArgumentParser(description="UDP Client")
    parser.add_argument('--addr', type=str, default='localhost', help="Server address (default: localhost)")
    parser.add_argument('--port', type=int, default=12345, help="Server port (default: 12345)")
    
    return parser.parse_args()

def configure_with_input():
    addr = input("Enter server address (default 'localhost'): ") or 'localhost'
    port = input("Enter server port (default 12345): ")
    port = int(port) if port else 12345
    
    return addr, port

if __name__ == "__main__":
    args = parse_arguments()
    
    if args.addr == 'localhost' and args.port == 12345:
        addr, port = configure_with_input()
    else:
        addr, port = args.addr, args.port
    
    start_server(addr=addr, port=port)