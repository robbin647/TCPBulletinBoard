#coding:utf-8

from socket import *
serverPort=16000
serverSocket=socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverPort))
print('The server is ready to receive...')
maxSession=3
while maxSession:
    message, clientAddress=serverSocket.recvfrom(2048)
    print('\nReceive message:',message.decode())
    outGoingMessage=input('Reply: ')
    serverSocket.sendto(outGoingMessage.encode(),clientAddress)
    maxSession=maxSession-1
serverSocket.close()