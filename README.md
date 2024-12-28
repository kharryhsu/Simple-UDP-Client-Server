# UDP-Client-Server

This project demonstrates a simple UDP server and client implementation in Python. The server listens for incoming messages from clients and allows communication. Both the server and client support user-configurable address and port settings via command-line arguments or interactive input.

---

## Screenshots

### Server Output
Here’s an example of the server output when a client connects and sends a message:
#### Server
![Screenshot 2024-12-28 181724](https://github.com/user-attachments/assets/2ae494b4-2cf4-40c1-870e-9884d882f936)

### Client Output
Here’s an example of the client output after connecting to the server:
#### Client 1
![Screenshot 2024-12-28 181733](https://github.com/user-attachments/assets/59f1b0f1-a59f-43a7-9fa2-548748ba93d8)

#### Client 2
![Screenshot 2024-12-28 181744](https://github.com/user-attachments/assets/afe543af-9bb7-465f-b6dc-199e169f967d)

---

## Features

### Server
- Listens for incoming UDP packets from client.
- Allows message exchange with clients.
- Supports command-line argument configuration or interactive input.
- Graceful shutdown with error handling.
- Uses multithreading to handle multiple clients concurrently.

### Client
- Sends UDP packets to the server using a specified address and port.
- Allows bidirectional communication with the server.
- Supports command-line argument configuration or interactive input.
- Handles errors and unexpected disconnections.

---

## Requirements
- Python 3.x

---

## How to Run

### Server
1. Navigate to the project directory.
2. Run the server script:
   ```bash
   python3 server.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 server.py --addr 127.0.0.1 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python3 server.py
   ```
   Example of prompted input:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```
### Client
1. Navigate to the project directory.
2. Run the server script:
   ```bash
   python3 client.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 client.py --addr 127.0.0.1 --port 12345
   ```
3. If no arguments are provided, the script will prompt for input:
   ```bash
   python3 client.py
   ```
   Example of prompted input:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```

---

## Notes

- Ensure the server is running before starting the client.

- For communication on the same machine, you can use `localhost` or `127.0.0.1` as the server address.

- If running on different machines, ensure the server's IP address is accessible from the client machine.

- The server uses multithreading to handle multiple clients concurrently. You can run multiple clients simultaneously for testing.

