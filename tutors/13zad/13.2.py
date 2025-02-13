from ipaddress import*
for mask in range(9,33):
    net1 = ip_network(f'215.181.200.27/{mask}',0)
    net2 = ip_network(f'215.181.192.0/{mask}',0)
    if net1 == net2:
        print(net1, net1.netmask)
    