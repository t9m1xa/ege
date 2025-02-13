from ipaddress import*
k = 0
for mask in range(9,33):
    net1 = ip_network(f'158.116.11.146/{mask}',0)
    net2 = ip_network(f'158.116.0.0/{mask}',0)
    if str(net1) == f'158.116.0.0/{mask}':
        k+=1
print(k)