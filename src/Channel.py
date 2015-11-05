

class Channel:
    def __init__(self, sock):
        self.sock = sock
        self.clientList = []
