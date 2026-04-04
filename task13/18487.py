from ipaddress import *

def f(ip):
    ip = f'{int(ip):032b}'
    return ip.count('1') > 15

for a in range(256):
    net = ip_network(f'192.214.{a}.184/27', 0)
    if all(f(ip) for ip in net):
        print(a)
        break
