#!/usr/bin/env python
import socket
from IPy import IP

def scan(ipaddress):
    converted_ip = check_ip(ipaddress)
    print('\n' + '[Scannipycharget]' + str(ipaddress))
    for port in range(1,100):
        scan_port(converted_ip, port)

def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip) #returns the IP address of the host.
def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(0.5) #for fast scanning
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('Port ' + str(port) + ' is open ' + ' : ' + str(banner.decode().strip('\n')))
        except:
            print('Port ' + str(port) + ' is open ')
    except:
        pass

ipaddress = input("Enter target ")
scan(ipaddress)


