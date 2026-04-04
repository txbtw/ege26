from ipaddress import *
def f(ip):
    ip = f'{int(ip):032b}'
    return ip[16:24].count('0') > ip[24:].count('0')
cnt = 0
for a in range(256):
    net = ip_network(f'246.81.65.{a}/255.255.255.224', False)
    if all(f(ip) for ip in net):
        cnt += 1
print(cnt)