#Código que scaneia uma rede

#Algoritmo escolhido no curso:
#   1º: Criar uma requisição ARP direcionada a broadcast solicitando um IP (v)
#   2º: Enviar o pacote e receber a resposta (v)
#   3º: Parse the response - extrair informação de uma estrutura (v)
#   4º: Mostrar o resultado(v)
#   5º: Criando uma lista de dicionários para melhorar a visualização da saída

import scapy.all as scapy 

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)  
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") 
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []

    for item in answered_list:
        client_dict = {'ip':item[1].psrc, 'mac':item[1].hwsrc} 
        clients_list.append(client_dict)  
    return clients_list

def print_result(results_list):
    print("--------------------------------------------------------")
    print("IP\t\t\tMAC ADDRESS")
    print("--------------------------------------------------------")

    for client in results_list:
        print(client['ip'] + '\t\t' + client['mac'])

scan_result = scan("10.0.2.1/24")
print_result(scan_result)