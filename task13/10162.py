from ipaddress import *

ip1 = ip_address('112.117.107.70')
ip2 = ip_address('112.117.121.80')
for mask in range(16, 25):
    net = ip_network(f'{ip1}/{mask}', 0)
    if ip2 in net.hosts() and ip1 in net.hosts():
        print(net.netmask)