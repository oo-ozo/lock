import socket


  # Create a socket object

s = socket.socket()
 
 
 # Define the port on which you want to connect

port = 12322


# connect to the server on local computer

s.connect(('10.6.219.217', port))


# receive data from the server

print s.recv(1024)
# close the connection
s.close()
