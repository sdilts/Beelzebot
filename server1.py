import socket
import threading
from queue import Queue
import client
import time
# import bodyControl as bc


#########################     RECEIVES THINGS
def wait_for_command(ip, port,roboControl, isStart=False):
    if wait_for_command.server == None:
        wait_for_command.server = Server(ip, port)
        wait_for_command.server.run()
        time.sleep(1)
    if isStart:
        client.say_phrase(ip, port, '', True, True)
    else:
        client.say_phrase(ip, port, '', True)
    time.sleep(1)
    found = False
    print("Waiting for command...")
    while not found:
        if not wait_for_command.server.recieved.empty():
            found = True;
            command = wait_for_command.server.recieved.get()

    print("wait_for_command just ran: ", command)
    do_the_thing(command, ip, port,roboControl, isStart)

wait_for_command.server = None

def do_the_thing(command, ip, port,roboControl, isStart=False):
    print("Command received in the place: ", command)
    if command == 'do your thing':
        pass
    elif command == 'dance':
        for i in range(5):
            roboControl.move_head_up()
            time.sleep(.5)
            roboControl.move_head_down()
            time.sleep(.5)
        for i in range(2):
            roboControl.turn_clockwise()
            roboControl.turn_counterClockWise()

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

    def __init__(self,ip, port):
        self.recieved = Queue()
        self.host = '127.0.0.1'
        self.port = 5012

    def stop(self):
        print("Stopping thread...")
        self.stopEvent.set()
        # self.mySocket.close()
        cl = client.Client("127.0.0.1", 5012, "", False)
        cl.start()
        cl.close()

    def commandLoop(self, conn):
        data = conn.recv(1024).decode()
        conn.close()
        self.recieved.put(data)

    def run(self):
        self.stopEvent = threading.Event()
        self.t = threading.Thread(target=self.serve)
        self.t.start()

    def serve(self):
        # atexit.register(self.stop);
        self.mySocket = socket.socket()
        self.mySocket.bind(('',self.port))
        self.mySocket.listen(1)
        while not self.stopEvent.wait(1):
            conn, addr = self.mySocket.accept()
            print("Connection from: " + str(addr))
            if not conn or not addr:
                print("your connection isn't working")
            self.commandLoop(conn)


        print("Closing everything...");
        self.mySocket.close()
        conn.close()
