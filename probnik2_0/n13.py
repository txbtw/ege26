from ipaddress import *
ipnet = ip_network('205.99.68.249/255.255.248.0', False)
print(ipnet[-2])