import socket
import sys
import time

s = socket.socket()
host = input("Please enter the hostname of the server: ")
port = 8080
s.connect((host,port))
print("Connected to the chat server")
while True:
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print("User 1: ", incoming_message)
        print("")
        message = input(">> ")
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
