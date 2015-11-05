import socket, logging, threading

class Socket:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)

    def accept():
        conn, addr  = s.accept()
        
