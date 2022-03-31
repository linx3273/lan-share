import socket
import src.msgs as msgs
from tqdm import tqdm 

def splitIP(ip):
    ADDR = ip.split(":")
    ADDR[1] = int(ADDR[1])
    return tuple(ADDR)



def client(ip,loc):
    pass
