import socket
import src.msgs as msgs
from tqdm import tqdm
import os
from pathlib import Path
import time
from colorama import Fore
import colorama

colorama.init(autoreset=True)

def __checkNoVerify(val):
    if val==0:
        msgs.msg("Connection requests will require confirmation")
    else:
        msgs.warnmsg("Connection requests will NOT require confirmation")

def __sendFile(conn,fileloc):
    SIZE = 1024
    filesize = os.path.getsize(fileloc)
    filename = Path(fileloc).name
    inf = f"{filename}?{filesize}"

    conn.send(inf.encode())
    time.sleep(1)
    bar = tqdm(range(filesize),"Sending: ",unit="B",unit_scale=True,unit_divisor=SIZE)
    with open(fileloc,"rb") as f:
        while True:
            data = f.read(SIZE)

            if not data:
                break

            conn.send(data)

            bar.update(len(data))
    return


def host(fileloc,noverify=0):
    sv = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sv.bind((socket.gethostbyname(socket.gethostname()),0))
    sv.listen()    
    ADDR = sv.getsockname()
    msgs.msg("Server listening on:"+ Fore.YELLOW +f"{ADDR[0]}:{ADDR[1]}")
    __checkNoVerify(noverify)
    flag = 1
    while flag:    
        conn,addr = sv.accept()

        if noverify==0:
            msgs.msg("Received request from "+Fore.RED+ f"{addr[0]}")
            c = msgs.inpmsg("Accept connection? [y/n]: ").upper()
            if c=="Y":
                conn.send("1".encode())
                __sendFile(conn,fileloc)
                flag = 0
                sv.close()
                msgs.msg("Closed Connection")
            else:
                conn.send("0".encode())
                conn.close()
                msgs.msg("Incoming request denied")
                msgs.msg("Server listening on:"+ Fore.YELLOW +f"{ADDR[0]}:{ADDR[1]}")
        else:
            conn.send("1".encode())
            msgs.msg(f"{addr[0]} connected")
            __sendFile(conn,fileloc)
            flag = 0
            sv.close()
            msgs.msg("Closed connection")