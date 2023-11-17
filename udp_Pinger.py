import time
from socket import *

# Set the server address and port
server_address = ('localhost', 12000)

# Create a UDP socket
client_socket = socket(AF_INET, SOCK_DGRAM)

# Set a timeout value of 1 second
client_socket.settimeout(1)

# Send 10 ping requests to the server
for sequence_number in range(1, 11):
    # Get the current time
    start_time = time.time()

    # Format the ping message
    message = f'Ping {sequence_number} {start_time}'

    try:
        # Send the ping message to the server
        client_socket.sendto(message.encode(), server_address)

        # Receive the server's response
        response, server_address = client_socket.recvfrom(1024)

        # Get the round trip time
        rtt = time.time() - start_time

        # Print the response and round trip time
        print(f'Response from {server_address[0]}: {response.decode()}')
        print(f'Round Trip Time: {rtt} seconds')

    except timeout:
        # Print "Request timed out" if no response within 1 second
        print(f'Request timed out')

# Close the socket
client_socket.close()