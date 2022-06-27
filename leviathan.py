#!/usr/bin/python3

import os
import nmap
import argparse
from pprint import pprint
from leviathan_classes import *

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
os.system("mkdir ./scans")

def div():
    print("#" * 50)

def quickScanTCP(target):
    arguments = "-T4 -oN ./scans/quick"
    div()
    print("Saving scan results to 'quick.nmap'")
    nm.scan(target.ip, arguments=arguments)
    parseScanData(target, nm, "tcp")

def fullScanTCP(target):
    arguments = "-p- -T5 -oN ./scans/full"
    div()
    print("Saving scan results to 'full.nmap'")
    nm.scan(target.ip, arguments=arguments)
    parseScanData(target, nm, "tcp")

def shortServiceScanTCP(target):
    arguments = "-T4 -sV -oN ./scans/service"
    div()
    nm.scan(target.ip, arguments=arguments)
    parseScanData(target, nm, "tcp")

def fullServiceScanTCP(target):
    arguments = "-T4 -p- -sV -oN ./scans/fullService"
    div()
    print("Saving scan results to 'fullService.nmap'")
    nm.scan(target.ip, arguments=arguments)
    parseScanData(target, nm, "tcp")

def quickScanUPD(target):
    arguments = "-T4 -sU -oN ./scans/quickUDP"
    div()
    print("Saving scan results to 'quickUDP.nmap")
    nm.scan(target.ip, arguments=arguments)
    parseScanData(target, nm, "udp")

def parseScanData(target, nm, protocol):
    target.hostname = nm[target.ip].hostname()
    target.state = nm[target.ip].state()
    for rport in nm[target.ip][protocol].keys():
        port = Port(rport, protocol,
            nm[target.ip][protocol][rport]["name"],
            nm[target.ip][protocol][rport]["product"], 
            nm[target.ip][protocol][rport]["version"]
            )
        target.add_port(port)
    
    print(target)



def menu():
    while True:
        print("MAIN MENU")
        print("Press 0 to exit")
        print("Press 1 for Quick TCP Scan")
        print("Press 2 for Full TCP Scan")
        print("Press 3 for Short TCP Service Scan")
        print("Press 4 for Full TCP Service Scan")
        print("Press 5 for Quick UDP Scan (SUDO)")

        div()

        choice = input (">>> ")

        match choice:
            case "clear":
                os.system("clear")
            case "0":
                break
            case "1":
                target = Host(args.target)
                quickScanTCP(target)
            case "2":
                target = Host(args.target)
                fullScanTCP(target)
            case "3":
                target = Host(args.target)
                shortServiceScanTCP(target)
            case "4":
                target = Host(args.target)
                fullServiceScanTCP(target)
            case "5":
                target = Host(args.target)
                quickScanUPD(target)
            case _:
                pass



menu()
