from ipaddress import *

for x in range(10,33):
    ipnet = ip_network(f'172.16.168.0/255.255.255.{x}', False)
    adr = f'{int(ipnet.network_address)}'
    if ipnet.num_addresses == 35 and adr.count('0') % 7 == 0:
        print(x)