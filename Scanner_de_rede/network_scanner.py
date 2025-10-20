#Código que scaneia uma rede

#Algoritmo escolhido no curso:
#   1º: Criar uma requisição ARP direcionada a broadcast solicitando um IP
#   2º: Enviar o pacote e receber a resposta
#   3º: Parse the response
#   4º: Mostrar o resultado

import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) 
    arp_request.show() #pode ser utilizado para qualquer pacote (só se utiliza em pacotes?)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #Cria um pacote Ethernetpara enviar ao endereço de broadcast e não apenas para um dispositivo apenas. Ether é a  interface utilizada = ethernet
    broadcast.show()
    #scapy.ls(scapy.Ether())
    #agora passa o endereço mac de destino com 'dest':
    #broadcast.dst = endereço    ou:     broadcast = scapy.Ether(dest="") e o endereço MAC tem o formato: ff:ff:ff:ff:ff:ff
    arp_request_broadcast = broadcast/arp_request #junto as informações em um pacote só
    #para ver mais detalhes do conteúdo do pacote recém criado:
    arp_request_broadcast.show()

scan("10.0.2.2/24")
#scan("10.0.2.2")