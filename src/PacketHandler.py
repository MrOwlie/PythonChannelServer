import threading

def handlePacket(data):
    data.decode("ASCII")
    print("DATA: " + str(data))
    #return data
