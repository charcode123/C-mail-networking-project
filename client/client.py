import socket
import json
import time
import os
def receive_json(conn):
    data = conn.recv(1024)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data
SERVER = "127.0.0.1"
PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
x=client.recv(1024)
print(x.decode())
time.sleep(1)
while True:
    os.system('cls')
    if input("Do you want to log in? (y/n): ") != "y":
        print("Bye!")
        break
    username=input("Username: ")
    password=input("Password: ")
    data={"username":username,"password":password}
    client.send(bytes(json.dumps(data),"UTF-8"))
    x=client.recv(1024)
    if x.decode()=="True":
        print("Login Successful")
        time.sleep(1)
        os.system('cls')
    else:
        print("Login Failed - Try Again")
        time.sleep(1)
        os.system('cls')
        continue
    while True:
        print("1. Send Email")
        print("2. View Inbox")
        print("3. View Sent")
        print("4. Logout")
        choice=input("Enter your choice: ")
        if choice=="1":
            client.send(bytes("1","UTF-8"))
            x=client.recv(1024)
            print(x.decode())
            to=input("To: ")
            y=client.send(bytes(to,"UTF-8"))
            if y==false:
                print("Invalid Username")
                continue
            subject=input("Subject: ")
            message=input("Message: ")
            data={"from":username,"to":to,"subject":subject,"message":message,"time":time.time()}
            client.send(bytes(json.dumps(data),"UTF-8"))
            x=client.recv(1024)
            print(x.decode())
        elif choice=="2":
            client.send(bytes("2","UTF-8"))
            x=receive_json(client)
            print(x)
        elif choice=="3":
            client.send(bytes("3","UTF-8"))
            x=receive_json(client)
            print(x)
        elif choice=="4":
            client.send(bytes("4","UTF-8"))
            x=client.recv(1024)
            print(x.decode())
            break            
client.close()