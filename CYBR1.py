# Import socket module and sys module to terminate the program
from socket import *
import sys
serverPort=80
# Create TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)
# Prepare server socket
# This means you need to assign a port number
# And bind socket to server address and port
# Hint: using “” as the server address will bind socket automatically
# to local host, and have socket listen to at most 1 connection at a time
#Fill in start
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('up on port:'), serverPort
#Fill in end
while True:
print(‘The server is ready to receive')
# Set up a new connection from the client
connectionSocket, addr = serverSocket.accept()#Fill in start serverSocket.accept #Fill in end
# If an exception occurs during the execution of try clause
# the rest of the clause is skipped
# If the exception type matches the word after except
# the except clause is executed
try:
# Receives the request message from the client
# Hint: remember to specify buffer size and to
# convert message to string
message = connectionSocket.recv(1024) #Fill in start #Fill in end
# Extract the path of requested object from message
# The path is the second part of HTTP header
# To do this, use the Python split function
# Also, because extracted path of the HTTP request includes
# a character '\', read the path from the second character
#Fill in start
print message, '::', message.split()[0], ':', message.split()[1]
filename = message.split()[1]
print filename, '||', filename[1:]
f = open(filename[1:])
#Fill in end
# Store the content of requested file in a temporary buffer
outputdata = f.read()#Fill in start #Fill in end
# Send the HTTP response header line to the connection socket
#Fill in start
print outputdata
connectionSocket.send('\nHTTP/1.1 200 OK\n\n')
connectionSocket.send(outputdata)
#Fill in end
#Send the content of the requested file to the connection socket
for i in range(0, len(outputdata)):
connectionSocket.send(outputdata[i].encode())
connectionSocket.send("\r\n".encode())
# Close the client connection socket
connectionSocket.close()
except IOError:
#Send response message for file not found
#Fill in start
connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')
#Fill in end
#Close client socket
#Fill in start
connectionSocket.close()
#Fill in end
serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data
