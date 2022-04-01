sudo apt install python3

python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
python3 -m venv env

source env/bin/activate
which python

python3 -m pip install colorama
python3 -m pip install tqdm
python3 -m pip install pyinstaller
