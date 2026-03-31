from ipaddress import *
cnt = 0
ipnet = ip_network('172.16.128.0/255.255.192.0', False)
for i in ipnet:
    if int(i) % 2 != 0:
        cnt += 1
print(cnt)