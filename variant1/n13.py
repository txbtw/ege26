from ipaddress import *

ipnet = ip_network('73.148.145.65/255.224.0.0', False)

print(ipnet[-2])