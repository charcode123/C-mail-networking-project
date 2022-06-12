import socket
import json
import time
import os
def receive_json(conn):
    data = conn.recv(4096)
    data = data.decode('utf-8')
    data = json.loads(data)
    return data
def receive_data(conn):
    data = conn.recv(4096)
    data = data.decode('utf-8')
    return data     
SERVER = "127.0.0.1"
PORT = 12345
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((SERVER, PORT))
x=receive_data(client)
print(x)
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
    x=receive_data(client)
    if x=="True":
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
            x=receive_data(client)
            print(x)
            to=input("To: ")
            y=client.send(bytes(to,"UTF-8"))
            if y==False:
                print("Invalid Username")
                continue
            subject=input("Subject: ")
            message=input("Message: ")
            data={"from":username,"to":to,"subject":subject,"message":message,"time":time.time()}
            client.send(bytes(json.dumps(data),"UTF-8"))
            x=receive_data(client)
            print(x)
        elif choice=="4":
            client.send(bytes("4","UTF-8"))
            x=receive_data(client)
            print(x)
            break 
        elif choice=="2" or choice=="3":
            client.send(bytes(choice,"UTF-8"))
            x=receive_json(client)
            for i in x:
                print("----------------------------------------------------")
                print("from:",i['from'])
                print("to:",i['to'])
                print("subject:",i['subject'])
                print("message:",i['message'])
                print("time:",time.strftime('%A, %Y-%m-%d %H:%M:%S', time.localtime(i['time'])))
                print("-----------------------------------------------------")
            

client.close()