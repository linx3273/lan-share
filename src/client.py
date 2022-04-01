import socket
import src.msgs as msgs
from tqdm import tqdm 
from pathlib import Path
import os

def __splitIP(ip):
    ADDR = ip.split(":")
    ADDR[1] = int(ADDR[1])
    return tuple(ADDR)

def __getFile(conn,loc):
    SIZE = 1024
    msgs.msg("Waiting for file")
    data = conn.recv(SIZE).decode()
    data = data.split("?")
    filename,filesize = data[0],int(data[1])
    msgs.msg(f"Receiving {filename} - [{filesize} Bytes]")

    bar = tqdm(range(filesize),"Receiving: ",unit="B",unit_scale=True,unit_divisor=SIZE)

    loc+=f"/{filename}"
    
    with open(loc,"wb") as f:
        while True:
            data = conn.recv(SIZE)

            if not data:
                if os.name == "nt":
                    os.system(f"start {Path(loc).parent}")
                else:
                    os.system(f"xdg-open {Path(loc).parent}")
                break

            f.write(data)
            bar.update(len(data))


def client(ip,loc):
    SIZE = 1024

    conn = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    conn.connect(__splitIP(ip))
    
    data = conn.recv(SIZE).decode()
    if int(data)==1:
        msgs.msg("Connection Accepted")
        __getFile(conn,loc)
        msgs.msg("Connection")
        conn.close()
    else:
        msgs.msg("Connection Denied")
        return



