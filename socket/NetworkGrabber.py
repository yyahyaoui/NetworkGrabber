import socket
import sys
import os
from __builtin__ import str

def retBanner (ip, port):
    try:
        socket.setdefaulttimeout(2)
        s= socket.socket()
        s.connect((ip, port))
        banner = s.recv(1024)
        return banner
    except:
        return
def checkVulns(banner, filename):
    f = open(filename,'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print "[+++++++] banner is vulnerable: %s" %str(banner)
    
def main():
    if (len(sys.argv) == 2):
        filename = sys.argv[1]
        if not os.path.isfile(filename):
            print "[-] Filename %s don't exists" %str(filename)
            exit(0)
        if not os.access(filename , os.R_OK):
            print "[-] Filename %s : access denied!" %str(filename) 
            exit(0)
        print "Reading vulnerabilities form %s" %str(filename)
    else:
        print "[-] Usage: python %s <vuln_file>" %str(sys.argv[0])
        exit(0)
    
    portList = [21,22,25,80,110,443]
    for x in range(130,140):
        for port in portList:
            ip = "192.168.47."+str(x)
            banner = retBanner(ip, port)
            if banner:
                print "[+] banner for ip: %s and port %s is: %s" %(ip, str(port), str(banner))
                checkVulns(banner, filename)
                  
if __name__ == '__main__':
        main()