import socket 
s = socket.socket()
port = 9801 
s.connect(('127.0.0.1', port)) 
print(s.recv(1024)) 
s.close()
