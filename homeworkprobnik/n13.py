from ipaddress import *

net = ip_network('68.203.243.87/255.255.224.0', 0)
print(net[-2])
#780