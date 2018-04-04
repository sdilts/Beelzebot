import socket
import client


#########################     RECEIVES THINGS
def wait_for_command(ip, port, isStart=False):
    client.say_phrase(ip, port, '', True)
    server = Server(isStart, ip, port)
    command = server.run()
    do_the_thing(command)


def do_the_thing(command):
    pass

class Server:
    
    def __init__(self,ip, port, isStart):
        self.host = '127.0.0.1'
        self.port = 5012
        self.anIP = ip
        self.anPort = port
        self.mySocket = socket.socket()
        self.mySocket.bind(('',self.port))
        self.isStart = isStart

    def run(self):
        self.mySocket.listen(1)
        conn, addr = self.mySocket.accept()
        print("Connection from: " + str(addr))
        #comeonman = "l\t"
        #conn.send(comeonman.encode())
        while True:
            data = conn.recv(1024).decode()
            if not data:
                pass
            else:
                print("from connected user: " + str(data))
                data = str(data)
                data = data.strip()
                if data == 'start' and isStart:
                    conn.close()
                    return data
                elif data == 'do a thing':
                    conn.close()
                    return data
                else:
                    wait_for_command(self.anIP, self.port, '', True)

        
        conn.close()
        return data


