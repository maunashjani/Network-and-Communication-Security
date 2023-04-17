import socket
import ssl

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Enable SSL/TLS
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

# Bind the socket to a local address and port
server_address = ('localhost', 8443)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

print("Waiting for a connection...")

while True:
    # Wait for a connection
    connection, client_address = sock.accept()
    secure_connection = None
    
    try:
        print("Connection from", client_address)

        # Wrap the socket with SSL/TLS
        secure_connection = context.wrap_socket(connection, server_side=True)
        
        # Receive data from the client
        data = secure_connection.recv(1024)
        print("Received:", data)

        # Send a response to the client
        message = "Hello, client!"
        secure_connection.sendall(message.encode('utf-8'))
        
    except ssl.SSLError as e:
        print("SSL Error:", e)
        
    finally:
        # Close the SSL/TLS connection
        if secure_connection is not None:
            secure_connection.close()
