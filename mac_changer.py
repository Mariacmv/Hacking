# Codigo que altera o endereco mac de um dispositivo


import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", dest="mac_address", help="New MAC address")
#Os dois primeiros argumentos indicam os comandos que o usuário pode utilizar para adicionar argumentos através de -i ou --interface
#A informação que o usuário armazenar deve ser guardada em 'interface' e se o usuário precisar de ajuda mostre a mensagem de ajuda

parser.parse_args() #Quero que faça o parse

interface = input('Digite a interface desejada: ')
mac_address = input('Digite o novo endereco MAC: ')

print("[+] Changing interface for:",interface, "to " +mac_address)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw ether', mac_address])
subprocess.call(['ifconfig', interface, 'up'])
