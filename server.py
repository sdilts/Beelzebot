import socket

#########################     RECEIVES THINGS

def Main():
    host = input("ip addr: ")
    port = int(input("port: "))

    

    mySocket = socket.socket()
    #mySocket.connect((host,port))
    mySocket.bind(('',port))

    #how many requests you can queue
    mySocket.listen(1)

    #connection and address from client
    conn, addr = mySocket.accept()
    print("Connected!")
    
    while True:
        data = conn.recv(1024).decode()
        
        if not data:
            pass
        else:
            print("from connected user: " + str(data))
            data = str(data)
        
        

    conn.close()
    #mySocket.close()

if __name__ == '__main__':
    Main()
