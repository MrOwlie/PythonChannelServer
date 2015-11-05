import threading, socket
from Client import Client

class ClientHandler:
    def __init__(self, sock):
        self.sock = sock
        self.clientList = []

    def newClient(self):
        while True:
            client = self.sock.accept()
            print("Client Connected!")
            self.clientList.append(client)
            threading.Thread(target=client.read()).start()
            threading.currentThread
