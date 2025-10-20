#Código que scaneia uma rede

#Algoritmo escolhido no curso:
#   1º: Criar uma requisição ARP direcionada a broadcast solicitando um IP (v)
#   2º: Enviar o pacote e receber a resposta (v)
#   3º: Parse the response - extrair informação de uma estrutura
#   4º: Mostrar o resultado

import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #aqui o pacote está sendo enviado a um endereço broadcast, porém é possível direcionar com certeza para um dispositivo específico
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1)[0]
    #print(answered_list.summary())
    #print(unanswered_list.summary()) 

    for item in answered_list:
        print(item[1].psrc) #printa o endereço ip de quem respondeu
        print(item[1].hwsrc) #printa o endereço mac de quem respondeu
        print("----------------------------------------------------")

scan("10.0.2.1/24")
#scan("10.0.2.2")