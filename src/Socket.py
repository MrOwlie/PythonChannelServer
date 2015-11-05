import socket, threading
from Client import Client

class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.sock.bind((self.host, self.port))
        self.sock.listen(1)

    def accept(self):
        conn, addr  = self.sock.accept()
        client = Client(conn, addr)
        return client
