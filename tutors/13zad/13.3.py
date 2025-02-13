from ipaddress import*

net = ip_network('235.86.56.0/255.255.248.0',0)
k=0
for ip in net:
    b = format(int(ip),'32b')
    if b[-2:] == '11':
        k+=1

print(k)