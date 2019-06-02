import zmq
import time


# global loggedUsers
loggedUsers = {"abebe":"chube"}
communicatingUsers = {}

servPort = input("Please enter the port number on which you want to run the server: ")
servPort = int(servPort)

context = zmq.Context()
socket = context.socket(zmq.REP)


def bindServer(port=5000):
    socket.bind("tcp://*:%i" % port)


def messageFilter(message):
    message = str(message, 'utf-8')
    intitialStep = message.split("][")
    for i in range(0, len(intitialStep)):
        intitialStep[i] = intitialStep[i].replace("[", "").replace("]", "").strip()

    return intitialStep

def doTaskFromFilter(filterredMessage):
    if(filterredMessage[0] == "startchat"):
        client = filterredMessage[3].split(":")
        loggedUsers[client[1]] = client[0] 

        # onlineUsers = loggedUsers
        # onlineUsers.pop(client[1])
        # message = onlineUsers

        socket.send_string(str(loggedUsers))

    elif(filterredMessage[0] == "chatsmn"):
        client = filterredMessage[3].split(":")
        # clientSocket = context.socket(zmq.REQ)
        # clientSocket.connect("tcp://%s:%s" % (client[0],client[1]))
        communicatingUsers[client[2]] = filterredMessage[1]
        #loggedUsers.pop(client[2]).pop(filterredMessage[1])

        socket.send_string("Connected to %s, write a message to send him \n" % filterredMessage[1])
        

    # elif(filterredMessage[0] == "Sendmessgae"):

    # elif(filterredMessage[0] == "closechat"):

    else:

        socket.send_string("already connected")



bindServer(servPort)

while True:
    message = socket.recv()
    doTaskFromFilter(messageFilter(message))

    # time.sleep(1)
