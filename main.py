import sys
import src.usage as usage

if __name__=="__main__":
    if len(sys.argv)!=2:
        if len(sys.argv)==1:
            print("Error: Missing arguments")
        else:
            print("Error: Too many arguments provided")
        print(usage.inf())
    else:
        if sys.argv[1]=="help" or sys.argv[1]=="h":
            print(usage.inf())
        elif sys.argv[1]=="client" or sys.argv[1]=="c":
            print("Launched as a Client")
        elif sys.argv[1]=="host" or sys.argv[1]=="s":
            print("Launched as a Host")
        else:
            print(usage.inf())       
