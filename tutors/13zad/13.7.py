from ipaddress import*

for mask in range(24,33):

    net1 = ip_network(f'121.171.5.70/{mask}',0)
    net2 = ip_network(f'121.171.5.107/{mask}',0)
    if net1 == net2:
        print(net1,2**(32-mask))