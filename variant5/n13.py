from ipaddress import *

for mask in range(10, 31):
    ipnet = ip_network(f'153.202.16.37/{mask}', False)
    print(ipnet.netmask)