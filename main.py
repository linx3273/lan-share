import sys
import src.msgs as msgs
import src.usage as usage
import src.host as host
import src.client as client
import re
import os
from pathlib import Path

def main():
    # ipMatch = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    ipMatch = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]+$"
    currentDir =  Path().cwd().as_posix()

    if len(sys.argv)==1:
        print(usage.inf())
    else:
# HELP
        if sys.argv[1]=="--help" or sys.argv[1]=="-h":
            print(usage.inf())

#  CLIENT MODE CLI HANDLING
        elif sys.argv[1]=="client" or sys.argv[1]=="c":
            if len(sys.argv)>2:
                if sys.argv[2]=="--help" or sys.argv[2]=="-h":
                    print(usage.clientinf())
                elif re.search(ipMatch,sys.argv[2]):
                    if len(sys.argv)>3:
                        if os.path.isdir(sys.argv[3]):
                            client.client(sys.argv[2],Path(sys.argv[3]).as_posix())
                        else:
                            msgs.errmsg("Directory not found")
                    else:
                        client.client(sys.argv[2],currentDir)
                else:
                    msgs.errmsg("Invalid argument/IP address provided. Run 'lshare client --help")
            else:
                msgs.errmsg("Missing arguments. Run 'lshare client --help'")

# SEVER MODE CLI HANDLING
        elif sys.argv[1]=="host" or sys.argv[1]=="s":
            if len(sys.argv)>2:
                if sys.argv[2]=="--help" or sys.argv[2]=="-h":
                    print(usage.hostinf())
                elif os.path.isfile(sys.argv[2]):
                    if len(sys.argv)>3:
                        if sys.argv[3]=="set-verify":
                            host.host(Path(sys.argv[2]).as_posix(),1)
                        else:
                            msgs.errmsg("Invalid argument provided. Run 'lshare host --help'")
                    else:
                        host.host(Path(sys.argv[2]).as_posix(),0)
                else:
                    msgs.errmsg("Invalid argument/File not found. Run 'lshare host --help'")
            else:
                msgs.errmsg("Missing arguments. Run '<program> host --help'")

# FAIL CASE
        else:
            msgs.errmsg("Invalid arguments provided. Run 'lshare --help'")


if __name__=="__main__":
    main()