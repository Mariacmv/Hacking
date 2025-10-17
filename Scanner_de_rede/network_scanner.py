#Código que scaneia uma rede

import scapy.all as scapy 

def scan(ip):
    scapy.arping(ip)

scan("10.0.2.2/24")
#scan("10.0.2.2")