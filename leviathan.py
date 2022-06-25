#!/usr/bin/python3

import nmap
import argparse
import os
from pprint import pprint
import pandas as pd

print("""
  _      ________      _______       _______ _    _          _   _ 
 | |    |  ____\ \    / /_   _|   /\|__   __| |  | |   /\   | \ | |
 | |    | |__   \ \  / /  | |    /  \  | |  | |__| |  /  \  |  \| |
 | |    |  __|   \ \/ /   | |   / /\ \ | |  |  __  | / /\ \ | . ` |
 | |____| |____   \  /   _| |_ / ____ \| |  | |  | |/ ____ \| |\  |
 |______|______|   \/   |_____/_/    \_\_|  |_|  |_/_/    \_\_| \_|
                                                                   
Made by xts-sec (https://github.com/xts-sec)
""")

parser = argparse.ArgumentParser(description='An offensive security tool which automates an engagement as far as possible, including scanning, enumeration, and exploitation.')

parser.add_argument("target", type=str)

args = parser.parse_args()

nm = nmap.PortScanner()

def div():
    print("#" * 50)

def quickScanTCP(target):
    div()
    nm.scan(target, arguments="")
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        for port in lport:
            print('port : %s' % (port))
    div()

def serviceScanTCP(target):
    div()
    nm.scan(target, arguments="-sV")
    for host in nm.all_hosts():
        print('Host : %s (%s)' % (host, nm[host].hostname()))
        print('State : %s' % nm[host].state())

    for proto in nm[host].all_protocols():
        print('Protocol : %s' % proto)
        lport = nm[host][proto].keys()
        for port in lport:
            print('port : %s\tService : %s\tVersion : %s' % (port, nm[host][proto][port]['name'], nm[host][proto][port]['product'] + " " + nm[host][proto][port]['version']))
    div()

def menu():
    while True:
        print("MAIN MENU")
        print("Press 0 to exit")
        print("Press 1 for quick tcp scan")
        print("Press 2 for Service Scan")

        div()

        choice = input (">>> ")

        match choice:
            case "0":
                break
            case "1":
                quickScanTCP(args.target)
            case "2":
                serviceScanTCP(args.target)
            case _:
                pass

menu()
