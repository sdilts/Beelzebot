import socket
import time

def say_phrase(hostIP, port, data, waitForTalking, isStart=False):
    client = Client(hostIP, port, data, waitForTalking, isStart)
    client.start()
    client.close()
    if waitForTalking:
        time.sleep(1)

class Client:

    def __init__(self, hostIP, port, data, isWait, isStart=False):
        self.host = hostIP
        self.port = int(port)
        self.mySocket = socket.socket()
        print("Connecting!")
        self.mySocket.connect((self.host,self.port))
        #self.toSend = False
        if isWait:
            self.data = "l\t"
        elif isWait and isStart:
            self.data = "l\tq"
        else:
            self.data = "s\t"
        self.data = self.data + data

    def start(self):
        self.data = str(self.data)
        print("sending: " + str(self.data))
        self.mySocket.send(self.data.encode())
        #self.toSend = False

    def close(self):
        self.mySocket.close()
