import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serverAddress = ("localhost", 8001)
print("Connecting to :" + str(serverAddress[0]) + ":" + str(serverAddress[1]))
sock.connect(serverAddress)
print("Connected")
message = input("Input: ")
sock.send(message.encode('ASCII'))
