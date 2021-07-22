import socket 
s = socket.socket() 
port = 9801 
msg = 'Connection Successful' 
s.bind(('', port)) 
print(f"Binded to port {port}") 
s.listen(5) 
print("Waiting for Connection") 
while 1: 
    conn, addr = s.accept() 
    print(f"Connected from {addr}") 
    conn.send(msg.encode()) 
    conn.close()
