from ipaddress import *

cnt = 0
ipnet = ip_network('172.16.192.0/255.255.192.0')
for ip in ipnet:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 5 != 0:
        cnt += 1
print(cnt)