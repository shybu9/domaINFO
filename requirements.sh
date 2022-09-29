#!/bin/bash
apt-get install python3
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --prefix=/usr/local/
python3 -m ensurepip --default-pip
python3 -m pip install whois
python3 -m pip  install requests
python3 -m pip install argparse
python3 -m pip install dnspython
python3 -m pip install shodan
python3 -m pip install colorama
python3 -m pip install socket
python3 -m pip install python-whois
