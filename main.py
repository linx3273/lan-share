import sys
import src.msgs as msgs
import src.usage as usage
import src.host as host
import re
import os

def main():
    # ipMatch = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"
    ipMatch = "^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5]):[0-9]+$"
    currentDir = "./" 

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
                            pass # path provided client
                        else:
                            msgs.errmsg("Directory not found")
                    else:
                        pass    # default path client
                else:
                    msgs.errmsg("Invalid Argument/IP address provided. Run '<program> client --help")
            else:
                msgs.errmsg("Missing Arguments. Run '<program> client --help'")

# SEVER MODE CLI HANDLING
        elif sys.argv[1]=="host" or sys.argv[1]=="s":
            if len(sys.argv)>2:
                if sys.argv[2]=="--help" or sys.argv[2]=="-h":
                    print(usage.hostinf())
                elif os.path.isfile(sys.argv[2]):
                    if len(sys.argv)>3:
                        if sys.argv[3]=="set-verify":
                            pass # set-verify ON host
                        else:
                            msgs.errmsg("Invalid argument provided. Run '<program> host --help'")
                    else:
                        pass    # set-verify OFF host
                else:
                    msgs.errmsg("Invalid Argument/File not found. Run '<program> host --help'")
            else:
                msgs.errmsg("Missing Arguments. Run '<progra> host --help'")

# FAIL CASE
        else:
            msgs.errmsg("Invalid Arguments Provided. Run '<program> --help'")


if __name__=="__main__":
    main()