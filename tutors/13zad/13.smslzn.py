from ipaddress import*

net = ip_network('172.16.8.0/255.255.252.0',0)
print(net, (2**10)//33)