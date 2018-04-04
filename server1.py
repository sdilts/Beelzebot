import socket

#########################     RECEIVES THINGS
def wait_for_command(isStart=False):
    server = Server(isStart)
    command = server.run()
    do_the_thing(command)


def do_the_thing(command):
    pass

class Server:
    
    def __init__(self, isStart):
        self.host = '127.0.0.1'
        self.port = 5012
        self.mySocket = socket.socket()
        self.mySocket.bind((host,port))
        self.isStart = isStart

    def run(self):
        self.mySocket.listen(1)
 	conn, addr = self.mySocket.accept()
        print("Connection from: " + str(addr))
        while True:
            data = conn.recv(1024).decode()
        
            if not data:
                pass
            else:
                print("from connected user: " + str(data))
                data = str(data)
                if data == 'start' and isStart:
                    conn.close()
                    return data
                elif data == 'do a thing'
                    conn.close()
                    return data

        
        conn.close()
        return data


