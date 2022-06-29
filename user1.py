import socket
import sys
import time

s = socket.socket()
host = socket.gethostname()
print("Server Will Start On Host: ", host)
port = 8080
s.bind((host,port))
print("")
print("Server succesfully completed binding to host and port")
print("")
s.listen(1)
conn, addr = s.accept()
print(addr, "Has connected to the server and is now online")
print("")
while True:
        message = input(">> ")
        message = message.encode()
        conn.send(message)
        print("message has been sent...")
        print("")
        incoming_message = conn.recv(1024)
        incoming_message = incoming_message.decode()
        print("User 2: ", incoming_message)
        print("")
