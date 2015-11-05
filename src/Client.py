import threading
from PacketHandler import handlePacket
class Client:
    def __init__(self, connection, address):
        self.connection = connection;
        self.address = address;

    def read(self):
        while True:
            data = self.connection.recv(10000)
            if data and (data != ""):
                threading.Thread(target=handlePacket, args=(data,)).start()
