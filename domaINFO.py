import whois
import dns.resolver
import sys
import socket
import argparse
import requests
import shodan
from colorama import init, Fore

# COLOURS...
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
blue = Fore.LIGHTBLUE_EX
highlight = Fore.MAGENTA
reset = Fore.RESET
init()

argparse = argparse.ArgumentParser(description=blue + "this tool is for getting details of a domain" + reset,
                                   usage="python {} -d or --domain <{}name of the domain{}> , -i <{}ip address{}> ,"
                                         " -o <{}save o/p result in file{}>".format(sys.argv[0], highlight, reset,
                                                                                    highlight, reset, highlight, reset))
argparse.add_argument("-d", "--domain", help=green + "enter the domain name after -d for searching" + reset,
                      required=True)
argparse.add_argument("-i", "--ip", help=green + "enter the ip address for shodan search" + reset)
argparse.add_argument("-o", "--oA", help=green + "enter a filename to save the output result" + reset)

args = argparse.parse_args()
domain = args.domain
ip = args.ip
oA = args.oA

# DOMAIN_DETAILS
domain_result = ''  # variable for output
print(blue + "\n[+] FETCHING_DOMAIN_DETAILS..... ")
try:
    who = whois.query(domain)
    print("\n[+] domain scanning completed....." + reset)
except:
    print(red + "\n[-] try to enter more persistent domain name.."
                "\n [*] or try reinstalling whois module")
try:
    domain_result += ("[+]                 NAME :"+highlight+"{}".format(who.name)) + '\n'
except:
    print(highlight + "\n[-] try to enter more persistent domain name")
try:
    domain_result += (green + "[+]         DOMAIN_OWNER : {}".format(who.owner)) + '\n'
except:
    pass
try:
    domain_result += ("[+]         DOMAIN_ADMIN : {}".format(who.admin)) + '\n'
except:
    pass
try:
    domain_result += ("[+]     DATE_OF_CREATION : {}".format(who.creation_date)) + '\n'
except:
    pass
try:
    domain_result += ("[+] REGISTRATION_DETAILS : {}; {}; {};".format(who.registrant_country, who.registrant,
                                                                      who.registrar)) + '\n'
except:
    pass
try:
    domain_result += ("[+]       CURRENT_STATUS : {}".format(who.status)) + '\n'
except:
    pass
try:
    domain_result += ("[+]   DATE_OF_EXPIRATION : {}".format(who.expiration_date)) + '\n'
except:
    pass
try:
    domain_result += ("[+]        OTHER_DOMAINS : {}".format(who.name_servers)) + '\n'
except:
    pass
print(green + domain_result + reset)  # PRINTING DOMAIN_DETAILS HERE.
# DOMAIN_RESOLVER
resolver_result = ''

print(blue + "\n[+] FETCHING DNS_LOOKUP......" + reset)

try:
    for a in dns.resolver.resolve(domain, 'A'):
        resolver_result += (green + "[+] A RECORD : {}".format(a.to_text())) + '\n'
except:
    resolver_result += red + "[-] A RECORD fetching failed......" + '\n'

try:
    for ns in dns.resolver.resolve(domain, 'NS'):
        resolver_result += (green + "[+] NS RECORD : {}".format(ns.to_text())) + '\n'
except:
    resolver_result += red + "[-] NS RECORD fetching failed......" + '\n'
try:
    for mx in dns.resolver.resolve(domain, 'MX'):
        resolver_result += (green + "[+] MX RECORD : {}".format(mx.to_text())) + '\n'
except:
    resolver_result += red + "[-] MX RECORD fetching failed......" + '\n'
try:
    for txt in dns.resolver.resolve(domain, 'TXT'):
        resolver_result += (green + "[+] TXT RECORD : {}".format(txt.to_text())) + '\n'
except:
    resolver_result += red + "[-] TXT RECORD fetching failed......" + '\n'

print(resolver_result + reset)  # PRINTING WHOLE RESULT HERE.

# LOCATION_DETAILS

print(blue + "\n[+] FETCHING LOCATION_DETAILS......" + reset)
location_result = ''
try:
    req = requests.request('GET', "https://geolocation-db.com/json/" + socket.gethostbyname(domain)).json()
except:
    location_result += red + "[-] LOCATION_DETAILS fetching failed....." + '\n'

try:
    location_result += ("[+] COUNTRY_CODE : {}".format(req['country_code'])) + '\n'
except:
    pass
try:
    location_result += ("[+] IPV4 : {}".format(req['IPv4'])) + '\n'
except:
    pass
try:
    location_result += ("[+] COUNTRY_NAME : {}".format(req['country_name'])) + '\n'
except:
    pass
try:
    location_result += ("[+] STATE : {}".format(req['state'])) + '\n'
except:
    pass
try:
    location_result += ("[+] LATITUDE : {}".format(req['latitude'])) + '\n'
except:
    pass
try:
    location_result += ("[+] LONGITUDE : {}".format(req['longitude'])) + '\n'
except:
    pass
try:
    location_result += ("[+] CITY : {}".format(req['city'])) + '\n'
except:
    pass
try:
    location_result += ("[+] POSTAL_CODE : {}".format(req['postal'])) + '\n'
except:
    pass

print(green + location_result + reset)  # PRINTING WHOLE GEO-LOCATION RESULT

# SHODAN SEARCH
shodan_result = ''
if ip:
    print(blue + "\n[+] PERFORMING SHODAN SEARCH......"
                 "\n[+] IP_ADDRESS :{} {}".format(highlight, ip) + reset)
    try:
        api = shodan.Shodan("2m2UDO9vez3HRzjfwLbKFbSKLH8IIMD9")  # SHODAN API_KEY
        output = api.search(ip)
        shodan_result += ("[+] TOTAL RESULTS FOUND : {}".format(output['total'])) + '\n \n'
        shodan_result += "[+} TOP 5 RESULTS:" + '\n\n'
    except:
        shodan_result += red + "[-] ERROR IN SHODAN SEARCH...." + '\n' + reset
    i = 0
    for outputs in output['matches']:
        if i < 6:
            shodan_result += ("IP :{} {}".format(highlight, outputs['ip_str']) + reset) + '\n'
            shodan_result += ("DATA : \n    {}".format(outputs['data'])) + '\n'
            shodan_result += " " + '\n'
            i = i + 1
    print(green + shodan_result + reset)
if oA:
    with open(oA, 'w') as file:
        file.write(blue + "[+] DOMAIN_DETAILS....\n" + reset + domain_result + '\n')
        file.write(blue + "[+] DNS_RESULTS.....\n" + reset + resolver_result + '\n')
        file.write(blue + "[+] LOCATION_DETAILS......\n" + reset + location_result + '\n')
        if ip:
            file.write(blue + "[+] SHODAN_RESULTS.......\n" + reset + shodan_result + "\n")
