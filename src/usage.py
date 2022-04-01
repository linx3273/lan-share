def inf():
    return '''Usage:
    lan-share <Option>

Option:
    client   c      Runs program with you connecting to a host
    host     s      Runs program with you hosting the connection
    --help  -h      Load this message


Source code: github.com/linx3273/lan-share/
    '''

def hostinf():
    return '''Usage
    lan-share host <Options> [no-verify]

Option:
    path            Enter absolute path of file that is to be sent to the client
    --help  -h      Loads this message

no-verify          [OPTIONAL FIELD] Will not ask for confirmation when receiving a connection.
                    If not provided it will ask for confirmation.
'''

def clientinf():
    return '''Usage
    lan-share client <Option> [PATH]

Option:
    <IP>            Enter the IP address of the host. FORMAT - IP:PORT
    --help  -h      Loads this message  

PATH                [OPTIONAL FIELD] Provide path to download the file to a specific directory.
                    If path is not provided the file will be downloaded to the current directory
'''