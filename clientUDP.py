#-*- coding:utf-8 -*-
from socket import *
serverName='DESKTOP-F9QNMH0'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
maxSession=3
while maxSession:
    message=input('Input outgoing message: ')
    clientSocket.sendto(message.encode(),(serverName, serverPort))
    responseMessage,serverAddress=clientSocket.recvfrom(2048)
    print('Receive message: ',responseMessage.decode(),'\n')
clientSocket.close()