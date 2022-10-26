# domaINFO
    ~THIS TOOL IS USED TO GATHER INFORMATION OF A GIVEN DOMAIN AND IP ADDRESS
    

![domainfo--help](https://user-images.githubusercontent.com/112984045/196380032-c54af914-6c89-4af2-96a2-ca105a68ee02.png)
<img  width=240 height = 240 src="https://user-images.githubusercontent.com/112984045/196399621-b5b2faff-0437-405e-8f3f-acf435d055a0.png" alt="screenshot here...." />
<img width=240 height = 240 src="https://user-images.githubusercontent.com/112984045/196399643-9231f3c5-82c6-43d0-90c9-70accecd404d.png" alt="screenshot here......" />
<img width=240 height = 240 src="https://user-images.githubusercontent.com/112984045/196402767-b834da0a-0b59-479b-b427-cef31c071029.png" alt="screenshot here......." />


<br>

## AVAILABLE ON :

* LINUX
* WINDOWS
* ANDROID (termux)


### TESTED ON :

* KALI LINUX (terminal)
* BLACKBOX UBUNTU (terminal)
* WINDOWS 11 (command prompt)
* ANDROID (termux)



### REQUIREMENTS :
* python3 (recommended) | python2 | python
* try bashing the requirements file : <br>
     ```bash
      sudo chmod +x requirements.sh
     ```
     ```bash
      sudo bash requirements.sh
     ```
     
* ### OR else go for every cmd in INSTALLATION



## INSTALLATION :

* `apt-get update`
* `apt-get upgrade -y`
* `pkg install python`
* `apt-get install python3`
* `pkg install git -y`
* `wget https://bootstrap.pypa.io/get-pip.py`
* `python3 get-pip.py --prefix=/usr/local/`
* `python3 -m ensurepip --default-pip`
* `python3 -m pip install argparse`
* `python3 -m pip install shodan`
* `python3 -m pip install dnspython`
* `python3 -m pip install socket`
* `python3 -m pip install colorama`
* `python3 -m pip install python-whois`
* `pkg install whois`
* `python3 -m pip install pyfiglet`
* `python3 -m pip install alive_progress`
* `pip install requests`
<br>  ~ ignore modules/packages which are present

## USAGE :

* ### downloading tool 
  ```bash
      sudo git clone https://github.com/shybu9/domaINFO.git
     ```
* ### syntax
  ```bash
      sudo python3 domaINFO  -d or --domain <name of the domain> , -i <ip address> , -o <o/p file name>
     ```
  
* ### examples

   `$ sudo python3 domaINFO  -d google.com`
   
   ` $ sudo python3 domaINFO  -d jntuh.ac.in -i 10.0.2.15`
   
   ` $ sudo python3 domaINFO  --domain facebook.com -ip 127.0.0.1 -oA domaINFO_output.txt`
    


### MODULES :
* python3 | pip
* whois
* dns.resolver
* sys
* socket
* argparse
* requests
* shodan
* colorama | Fore | init
* pyfiglet 
* time | sleep
* alive_progress | alive_bar

## FEATURES :
#### [*] All domain details.
#### [*] DNS LOOKUP for records.
#### [*] LOCATION details of domain
#### [*] SHODAN search of ip
#### [*] TOP 5 SHODAN search results of ip
#### [*] OUTPUT the result to file
#### [*] SMOOTH and CLEAR code
