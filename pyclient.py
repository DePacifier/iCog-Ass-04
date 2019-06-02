import zmq
import socket
import sys
from  multiprocessing import Process

server_message = ""
context = zmq.Context()

def startServer(portClientServer, messageAccepter):
    socketClientServer = context.socket(zmq.REP)
    socketClientServer.bind("tcp://*:%i" % portClientServer)

    while True:
        messageAccepter = socketClientServer.recv()

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]

    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP 



def connectToServer(socket, ip = "localhost", port = "5000"):
    socket.connect("tcp://%s:%s" % (ip,port))

def startClient():
    serverIP = input("Please provide the port number of the ip server: ")
    serverPort = input("Please provide the port number of the port server: ")
    userName = input("PLease provide a user name that you will use: ")
    IP = get_ip()

    print("Connecting to hello world server ...")
    socket = context.socket(zmq.REQ)

    connectToServer(socket, serverIP, serverPort)
    smnname = "teddy"

    clientserverportnum = "5555"

    #                 command, message, serveraddress, clientaddress
    connectMessage = "[startchat][''][%s:%s][%s:%s]" % (serverIP,serverPort,IP,userName)
    startchatwithsmn = "[chatsmn][%s][%s:%s][%s:%s:%s]" % (smnname,serverIP,serverPort,IP,clientserverportnum,userName)

    while True:
        print("------------------------------------")
        print("1 - show online users \n \
            \r2 <username>- start chat with user \n \
            \rexit - exit back from anything")
        print("------------------------------------")
        value = input("what do you want to do : ")

        if(value == "1"):
            socket.send_string(connectMessage)
            message = socket.recv()
            print("Recieved reply [%s]" % message)
        elif(str(value).startswith("2")):
            socket.send_string(startchatwithsmn)
            message = socket.recv()
            print("Recieved reply [%s]" % message)
            socket.send_string("hello")
        elif(value == "exit"):
            exit()
        else:
            print("invalid input")

    # for request in range(10):
    #     if(request == 0):
    #         socket.send_string(connectMessage)
    #         message = socket.recv()
    #         print("Recieved reply %s [%s]" % (request, message))
    #     elif(request == 1):
    #         socket.send_string(startchatwithsmn)
    #         message = socket.recv()
    #         print("Recieved reply %s [%s]" % (request, message))
    #         socket.send_string("hello")
    #     else:    
    #         message = socket.recv()
    #         print("Recieved reply %s [%s]" % (request, message))
    #         socket.send_string("hello")

startClient()