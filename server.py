import socket

#########################     RECEIVES THINGS

def Main():
    host = '127.0.0.1'
    port = 5012

    mySocket = socket.socket()
    mySocket.bind((host,port))
    #mySocket.connect((host,port))

    #how many requests you can queue
    mySocket.listen(1)

    #connection and address from client
    conn, addr = mySocket.accept()
    print("Connection from: " + str(addr))
    
    while True:
        data = conn.recv(1024).decode()
        
        if not data:
            pass
        else:
            print("from connected user: " + str(data))
            data = str(data)
        
        

    #conn.close()
    conn.close()

if __name__ == '__main__':
    Main()
