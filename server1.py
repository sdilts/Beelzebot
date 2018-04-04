import socket
import client
import time
import bodyControl as bc


#########################     RECEIVES THINGS
def wait_for_command(ip, port,roboControl, isStart=False):
    if isStart:
        client.say_phrase(ip, port, '', True, True)
    else:
        client.say_phrase(ip, port, '', True)
    time.sleep(1)
    server = Server(ip, port, isStart)
    command = server.run()
    server.close()
    time.sleep(.5)
    print("wait_for_command just ran: ", command)
    do_the_thing(command, ip, port,roboControl, isStart)


def do_the_thing(command, ip, port,roboControl, isStart=False):
    print("Command received in the place: ", command)
    if command == 'do your thing':
        pass
    elif command == 'dance':
       
        roboControl.turn_clockwise()
        time.sleep(2)
        roboControl.turn_counterClockWise()
        time.sleep(2)
        print('done dancing!')
        
    elif command == 'start' and isStart:
        pass
    elif isStart:
        time.sleep(.5)
        wait_for_command(ip, port,roboControl, True)
    else:
        time.sleep(.5)
        wait_for_command(ip, port, roboControl)

class Server:
    
    def __init__(self,ip, port, isStart):
        self.host = '127.0.0.1'
        self.port = 5012
        self.anIP = ip
        self.conn = None
        self.addr = None
        self.anPort = port
        self.mySocket = socket.socket()
        self.mySocket.bind(('',self.port))
        self.isStart = isStart

    def run(self):
        self.mySocket.listen(1)
        self.conn, self.addr = self.mySocket.accept()
        print("Connection from: " + str(self.addr))
        if not self.conn or not self.addr:
            print("your connection isn't working")
        #comeonman = "l\t"
        #conn.send(comeonman.encode())
        while True:
            data = self.conn.recv(1024).decode()
            if not data:
                pass
            else:
                print("from connected user: " + str(data))
                data = str(data)
                data = data.strip()
                self.conn.close()
                self.mySocket.close()
                return data

        self.mySocket.close()
        self.conn.close()
        return data


    def close(self):
        self.mySocket.close()
        self.conn.close()
