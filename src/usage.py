def inf():
    return '''Usage:
    program <Option>

Option:
    client   c      Runs program with you connecting to a host
    host     s      Runs program with you hosting the connection
    --help  -h      Load this message
    '''

def hostinf():
    return '''Usage
    program host [OPTIONAL]

Option:
    set-verify      Will ask for confirmation when receiving a connection
    --help  -h      Loads this message
    '''

def clientinf():
    return '''Usage
    program client <Option>

Option:
    <IP>            enter the IP address of the host
    --help  -h      Loads this message  
    '''