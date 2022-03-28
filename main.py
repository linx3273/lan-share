import sys
import src.msgs as msgs
import src.usage as usage
import src.host as host
import re

ipmatch = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

def main():
    if len(sys.argv)==1:
        print(usage.inf())
    else:
        if sys.argv[1]=="--help" or sys.argv[1]=="-h":
            print(usage.inf())

        elif sys.argv[1]=="client" or sys.argv[1]=="c":
            if len(sys.argv)==3:
                if sys.argv[2]=="--help" or sys.argv[2]=="-h":
                    print(usage.clientinf())
                else:
                    if re.search(ipmatch,sys.argv[2]):
                        pass
                    else:
                        msgs.errmsg("Invalid IP address")
            else:
                msgs.errmsg("Invalid/Missing Arguments. Run '<program> client --help'")      

        elif sys.argv[1]=="host" or sys.argv[1]=="s":
            if len(sys.argv)==2:
                host.host()
            else:
                if sys.argv[2]=="set-verify":
                    host.host(setverify=1)
                elif sys.argv[2]=="--help" or sys.argv[2]=="-h":
                    print(usage.hostinf())
                else:
                    msgs.errmsg("Invalid Arguments Provided. Run '<program> host --help'")

        else:
            msgs.errmsg("Invalid Arguments Provided. Run '<program> --help'")


if __name__=="__main__":
    main()