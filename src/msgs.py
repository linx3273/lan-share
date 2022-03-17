import colorama
from colorama import Fore


colorama.init(autoreset=True) # autoreset so that the color remains green only for that print line

# when an error has occured
def errmsg():
    print("[" + Fore.RED + "ERR" + Fore.RESET + "]",end=' ')

# when input is required in the current line
def inpmsg():
    print("[" + Fore.YELLOW + "INP" + Fore.RESET + "]",end=' ')

# default info message
def msg():
    print("[" + Fore.GREEN + "INF" + Fore.RESET + "]",end=' ')