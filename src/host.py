import socket
import src.msgs as msgs
from tqdm import tqdm

def checkSetVerify(val):
    if val==1:
        msgs.msg("Connection requests will require confirmation")
    else:
        msgs.msg("Connection requests will  require confirmation")


def host(fileloc,setverify=0):
    sv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind(socket.gethostbyname(socket.gethostname()),0)
    sv.listen()    
    ADDR = sv.getsockname()
    msgs.msg(f"Server Listening on: {ADDR[0]}:{ADDR[1]}")
    checkSetVerify(setverify)

    while True:
        msgs.inpmsg(">")

