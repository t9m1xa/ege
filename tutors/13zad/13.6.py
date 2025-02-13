from ipaddress import*

'''for mask in range(17,33):
    net1 = ip_network(f'61.58.73.42/{mask}',0)
    net2 = ip_network(f'61.58.75.136/{mask}',0)
    if net1 == net2:
        print(net1)
'''
k = 0
net = ip_network('61.58.73.42/22',0)
for ip in net.hosts():
    b = format(int(ip),'32b')
    if b.count('1') %2 == 1:
        k+=1
print(k)