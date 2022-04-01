# LAN SHARE
- Written on python 3.8.10

### Installing dependencies
- use `pip install -r .\requirements.txt` to download all the dependencies 

## Running the program
### Help
- use `python main.py --help` or `python main.py -h`

### Host mode
- `python main.py host <PATH> [no-verify]`
- [PATH] - absolute location of file that has to be shared
- [no-verify] - Optional field, if not mentioned the program will take user confirmation for connection requests

### Client Mode
- `python main.py <IP:PORT> [PATH]`
- [PATH] - Optional field, if not mentioned the program takes the current directory in which the terminal is


## NOTE
- as of now only files can be shared, incase an entire directory has to be shared, it must be compressed before sharing.
