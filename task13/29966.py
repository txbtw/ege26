from ipaddress import *

ipnet = ip_network('146.180.173.153/255.192.0.0', False)
print(ipnet[-2])
