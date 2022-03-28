import socket
import src.msgs as msgs

def checkSetVerify(val):
    if val==1:
        msgs.msg("Connection requests will require confirmation")
    else:
        msgs.msg("Connection requests will  require confirmation")


def host(setverify=0):
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    sv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind((IP,PORT))
    sv.listen()

    checkSetVerify(setverify)
    
    msgs.msg(f"Server Listenting on: {IP}")
    while True:
        msgs.inpmsg(">")