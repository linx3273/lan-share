import socket
import src.msgs as msgs

def host():
    IP = socket.gethostbyname(socket.gethostname())
    PORT = 5050
    sv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind((IP,PORT))
    sv.listen()
    msgs.msg(f"Server Listenting on: {IP}")
    while True:
        msgs.inpmsg(">")