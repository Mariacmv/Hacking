# Codigo que altera o endereco mac de um dispositivo


import subprocess

interface = input('Digite a interface desejada: ')
mac_address = input('Digite o novo endereco MAC: ')

print("[+] Changing interface for:",interface, "to " +mac_address)

#subprocess.call(f"ifconfig {interface} down", shell=True)
#subprocess.call(f"ifconfig {interface} hw ether {mac_address}", shell=True)
#subprocess.call(f"ifconfig {interface} up", shell=True)

subprocess.call(['ifconfig', interface, 'down'])
subprocess.call(['ifconfig', interface, 'hw ether', mac_address])
subprocess.call(['ifconfig', interface, 'up'])