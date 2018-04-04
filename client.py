import socket

def say_phrase(hostIP, port, data):
    client = Client(hostIP, port, data)
    client.start()
    client.close()

################################    SENDS THINGS
class Client:

    def __init__(self, hostIP, port, data):
        self.host = hostIP
        self.port = int(port)
        self.mySocket = socket.socket()
        print("Connecting!")
        self.mySocket.connect((self.host,self.port))
        #self.toSend = False
        self.data = "s\t"
        self.data = self.data + data



    #def say_phrase(self, phrase):
        #self.data = phrase
        #self.toSend = True

    def start(self):
       
        #while True:      
            
            #if not self.toSend:
               
            
        self.data = str(self.data)
        print("sending: " + str(self.data))
        self.mySocket.send(self.data.encode())
        #self.toSend = False

    def close(self):
        self.mySocket.close()


