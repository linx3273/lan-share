import socket
import src.msgs as msgs
from tqdm import tqdm
import os
from pathlib import Path

def __checkSetVerify(val):
    if val==1:
        msgs.msg("Connection requests will require confirmation")
    else:
        msgs.warnmsg("Connection requests will NOT require confirmation")

def __sendFile(conn,fileloc):
    SIZE = 1024
    filesize = os.path.getsize(fileloc)
    filename = Path(fileloc).name
    inf = f"{filename}?{filesize}"

    conn.send(inf.encode())
    bar = tqdm(range(filesize),"Sending: ",unit="B",unit_scale=True,unit_divisor=SIZE)
    with open(fileloc,"rb") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            conn.send(data)

            bar.update(len(data))
    return


def host(fileloc,setverify=0):
    sv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind((socket.gethostbyname(socket.gethostname()),0))
    sv.listen()    
    ADDR = sv.getsockname()
    msgs.msg(f"Server Listening on: {ADDR[0]}:{ADDR[1]}")
    __checkSetVerify(setverify)
    conn,addr = sv.accept()

    if setverify==1:
        print(f"Received request from {addr[0]}")
        c = input("Accept connection? [y/n]: ").upper()
        if c=="Y":
            conn.send("1".encode())
            __sendFile(conn,fileloc)
        else:
            conn.send("0".encode())
            sv.close()
            msgs.msg("Closed socket")
    else:
        conn.send("1".encode())
        __sendFile(conn,fileloc)
        sv.close()
        msgs.msg("Closed connection")