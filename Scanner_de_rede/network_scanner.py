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
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff") #aqui o pacote está sendo enviado a um endereço broadcast, porém é possível direcionar com certeza para um dispositivo específico
    arp_request_broadcast = broadcast/arp_request 
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    #print(answered_list.summary())
    #print(unanswered_list.summary()) 

    print("--------------------------------------------------------")
    print("IP\t\t\tMAC ADDRESS") #'\t' é um tab - espaço
    print("--------------------------------------------------------")

    clients_list = [] #crio uma lista que vai armazenar os conjuntos de valores em um dicionário

    for item in answered_list:
        client_dict = {'ip':item[1].psrc, 'mac':item[1].hwsrc} #crio o dicionário determinando quais valores serão armazenados e como
        clients_list.append(client_dict) #adiciono cada item do dicionário a lista 
        print(item[1].psrc + "\t\t" + item[1].hwsrc)  #junto para printar na mesma linha
    print(clients_list)

scan("10.0.2.1/24")
#scan("10.0.2.2")

#para mostrar menos informações sobre o processo, utiliza-se a função 'verbose=False'