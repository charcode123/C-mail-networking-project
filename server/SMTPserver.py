import socket, threading
import os
import json
import time
import user_authentication as ua
def receive_json(conn):
    data = conn.recv(1024)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data
def receive_data(conn):
    data = conn.recv(1024)
    data = data.decode('utf-8')
    return data    
class ClientThread(threading.Thread):
    def __init__(self,clientAddress,clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print ("New connection added: ", clientAddress)
        self.csocket.send(bytes("Connection estblished",'UTF-8'))
    def run(self):
        msg = ''
        while True:
            data=receive_json(self.csocket)
            x=ua.user_auth(data['username'],data['password'])
            if x==True:
                self.csocket.send(bytes("True","UTF-8"))
            else:
                self.csocket.send(bytes("False","UTF-8"))
                continue
            choice=receive_data(self.csocket)
            if choice=="1":
                to=receive_data(self.csocket)    
                

        print ("Client at ", clientAddress , " disconnected...")
LOCALHOST = "127.0.0.1"
PORT = 12345
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((LOCALHOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(2)
    clientsock, clientAddress = server.accept()
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()