# A simple socket listener I wrote in Python
# First Python code I have written

# Import the refrences
import socket
import sys

# Define the host & port
host = '127.0.0.1'
port = 6112

# Create the socket
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Log that the socket was created 
print('Socket has been successfully created.')

# Try to bind the socket
try:
	socket.bind((host, port))
except socket.error as error:
	# Log that the socket was not able to bind
	print('Socket bind failed - ' + error[1] + '')

# If there was no exception, log that the socket bind was successfull
print('Successful socket bind.')

# Start listening for socket connections
socket.listen(5)

# Log that it has started to listen for socket connections
print('Listening for connections.')

# Accept socket connections in a endless loop
while 1:
	connection, address = socket.accept()
	print('New connection accepted - ' + address[0] + '')

# Close the socket connection
socket.close()
