from ipaddress import *
mask = '255.255.255.192'
def f(ip):
    ip = f'{int(ip):032b}'
    return ip[:16].count('0') <= ip[16:].count('0')


for a in range(0, 256)[::-1]:
    ip_1 = ip_address(f'223.167.{a}.167')
    net = ip_network(f'223.167.{a}.167/{mask}', False)
    if ip_1 in net.hosts() and  all(f(ip) for ip in net):
        print(a)
        break