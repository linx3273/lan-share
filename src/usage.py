def inf():
    return '''Usage:
    lshare <Option>

Option:
    client   c      Runs program with you connecting to a host
    host     s      Runs program with you hosting the connection
    --help  -h      Load this message
    '''

def hostinf():
    return '''Usage
    lshare host <Options [set-verify]

Option:
    path            
    --help  -h      Loads this message

set-verify          [OPTIONAL FIELD] Will ask for confirmation when receiving a connection.
                    If not provided it will not ask for confirmation
'''

def clientinf():
    return '''Usage
    lshare client <Option> [PATH]

Option:
    <IP>            Enter the IP address of the host. FORMAT - IP:PORT
    --help  -h      Loads this message  

PATH                [OPTIONAL FIELD] Provide path to download the file to a specific directory.
                    If path is not provided the file will be downloaded to the current directory
'''