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
- Listens for incoming UDP packets from clients.
- Handles multiple clients concurrently using multithreading.
- Allows message exchange with clients.
- Supports address and port configuration via command-line arguments or interactive input.
- Provides error handling and graceful shutdown.

### Client
- Sends UDP packets to the server.
- Supports bidirectional communication with the server.
- Configurable via command-line arguments or interactive input.
- Handles errors and unexpected disconnections.

---

## Requirements
- Python 3.x

---

## Deployment

1. **Clone the Repository**
   
   Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/TCP-Clients-Server.git
   ```
2. **Navigate to the Project Directory**

   Change to the project directory:
   ```bash
   cd TCP-Clients-Server
   ```
3. **Run the Server**

   Start the server script:
   ```bash
   python3 server.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 server.py --addr 127.0.0.1 --port 12345
   ```
4. **Run the Client**

   Start the client script:
   ```bash
   python3 client.py --addr <server_address> --port <server_port>
   ```
   Example:
   ```bash
   python3 client.py --addr 127.0.0.1 --port 12345
   ```
5. **Interactive Input (Optional)**

   If no arguments are provided, the script will prompt for input. 
   Example:
   ```bash
   python3 server.py
   ```
   Prompted input example:
   ```bash
   Enter server address (default 'localhost'): 127.0.0.1
   Enter server port (default 12345): 12345
   ```

---

## Future Improvements

- Packet Header Implementation: Add packet headers for better data parsing and protocol handling.

- GUI Interface: Create a graphical user interface for improved usability and visualization.

---

## Notes

- Ensure the server is running before starting the client.

- Use `localhost` or `127.0.0.1` for communication on the same machine.

- For communication across different machines, ensure the server's IP address is accessible and firewall settings allow connections.
  
- The server logs the connection status of clients and uses multithreading to handle multiple clients simultaneously.
