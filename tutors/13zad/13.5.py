from ipaddress import*
k = 0
net = ip_network('122.159.136.144/255.255.255.248',0)
for ip in net:
    b = format(int(ip),'32b')
    if b.count('1') % 4 != 0:
        k+=1
print(k)

ip1 = ip_address('137.219.220.63')
print(f'{ip1:b}')