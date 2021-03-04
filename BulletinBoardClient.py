# -*- encoding:utf-8 -*-
#Student name: YANG Tianxia

from socket import *

'''Validate IP address and port number'''

flag=True
while flag:
    try:
        serverAddr=input("Please input BulletinBoardServer's IPv4 address: ")
        serverName=inet_aton(serverAddr)
    except OSError as e:
        print("Wrong IPv4 address:", e)
        continue
    else:
        flag=False

flag=True
while flag:
    serverPort=int(input("Please input BulletinBoardServer's port number: (it is 16000 in this question)"))
    if serverPort>=0 and serverPort<=65535:
        flag=False
    else:
        print("Wrong port number. Try again!")

'''Create socket and connect to server '''

mySocket=socket(AF_INET,SOCK_STREAM)
mySocket.settimeout(2.0)
try:
    print("IP address:",serverAddr,"  Port number",serverPort)
    print("connecting to the server...")
    mySocket.connect((serverAddr,serverPort))
except timeout as e:
    print("Connection failed: ",e)
    exit_input=''
    while exit_input=='':
        exit_input=input("press any key (and enter) to exit: ")
else:
    print("Successfully connected!")


while True:
    
    """Constantly ask for user command """
    usr_input=input()                                   #note that input() function will automatically trim '\n' off  
    
    if usr_input=="QUIT":
        usr_input=usr_input+"\n"
        mySocket.send(usr_input.encode())
        serverResponse=mySocket.recv(2048)
        print("server: ",serverResponse.decode())
        mySocket.close()                                #close the socket
        break
         
    elif usr_input=="POST":
        client_message=""                               #this is to store all client messages
        post_input="POST"
        while post_input!=".":
            client_message=client_message+post_input+"\n"
            print("client:",post_input)
            post_input=input()
        print("client: ",post_input)                    #this is when user types .\n 
        client_message=client_message+".\n"
        mySocket.send(client_message.encode())
        serverResponse=mySocket.recv(2048)              #if successful, server responds by "OK"
        print("server: ",serverResponse.decode())
    
    elif usr_input=="READ":
        print("client: ",usr_input)
        usr_input=usr_input+"\n"
        mySocket.send(usr_input.encode())
        try:
            while True:
                serverResponse=mySocket.recv(2048)
                server_message=serverResponse.decode()
                print("server: ",server_message)
                if server_message=='.':
                    break
        except timeout:
            continue
    
        ''''Error command '''
    elif not((usr_input=="QUIT") or (usr_input=="READ") or (usr_input=="POST")):
        print("client: ",usr_input)
        usr_input=usr_input+"\n"
        mySocket.send(usr_input.encode())
        serverResponse=mySocket.recv(2048)
        print("server: ",serverResponse.decode())
     


