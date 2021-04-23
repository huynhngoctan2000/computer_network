#Lib 
import psutil
import socket
import time

from socket import*
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind("",serverPort)
print("the server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode().clientAddress)



def makeMessage (idx):
    mess = "**1SEN#"+str(idx)+"**"
    return messages

def register(UDP):
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    timer = time.localtime()
    time_Info = str(timer.tm_mday)+"/"+str(timer.tm_mon)+"/"+str(timer.tm_year)+" "+str(timer.tm_hour)+":"+str(timer.tm_min)+":"+str(timer.tm_sec)
    reg = "**1DK#"+hostname+"#"+ip+"#"+str(UDP)+"#"+time_Info+"**"
    return reg