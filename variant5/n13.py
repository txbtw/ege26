from ipaddress import *


ip_host = ip_address('153.202.16.37')


for mask in range(16, 31):
    ipnet = ip_network(f'{ip_host}/{mask}', False)
    if ip_host in ipnet.hosts() and ip_address('153.202.16.32') == ipnet.network_address:
        print(sum(map(int, str(ipnet.netmask).split('.')[-2:])))