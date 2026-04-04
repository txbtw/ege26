from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('1') >= ip[16:].count('1')

for a in range(256)[::-1]:
    net = ip_network(f'116.242.{a}.26/255.255.255.224', 0)
    if all(f(ip) for ip in net):
        print(a)
        break