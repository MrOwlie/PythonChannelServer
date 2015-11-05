import threading
from Socket import Socket
from ClientHandler import ClientHandler

def main():
    sock = Socket('localhost',8001)
    clientHandler = ClientHandler(sock)

    clientAcceptThread = threading.Thread(target=clientHandler.newClient()).start()
    clientAcceptThread.run()
main()
