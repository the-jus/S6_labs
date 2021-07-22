import socket
import time

localIP="127.0.0.1"
localPort=20001
bufferSize=1024

msgFromServer =time.ctime(time.time())
bytesToSend =msgFromServer.encode('ascii')

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP,localPort))

print("UDP Server is Running")

while(True):
    bytesAddressPair =UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    clientMsg = "Message from Client:{}".format(message)
    clientIP = "Client IP address:{}".format(address)

    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)