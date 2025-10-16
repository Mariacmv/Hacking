# Codigo que altera o endereco mac de um dispositivo


import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address")
    parser.add_option("-m", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()

    if not options.interface:
        #Se não tiver valor para a variável interface
        parser.error("[-] É necessário informar a interface. --help para ajuda")
    elif not options.new_mac:
        #Se não tiver valor para a variável new_mac
        parser.error("[-] É necessário informar um endereço MAC. --help para ajuda")
    return options

def change_mac(interface, new_mac):
    print("[+] Changing interface for:",interface, "to " +new_mac)

    subprocess.call(['ifconfig', interface, 'down'])
    subprocess.call(['ifconfig', interface, 'hw ether', new_mac])
    subprocess.call(['ifconfig', interface, 'up'])

 
options = get_arguments()
change_mac(options.interface, options.new_mac)

