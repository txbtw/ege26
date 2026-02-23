from ipaddress import ip_network

ipnet = ip_network('42.172.106.203/255.255.252.0', 0)
print(ipnet[-2])