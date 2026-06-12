from ipaddress import *

ipnet = ip_network('112.160.0.0/255.240.0.0', False)
cnt = 0
for ip in ipnet:
    ip = f'{int(ip):032b}'
    if ip.count('1') % 5 == 0:
        cnt += 1

print(cnt)