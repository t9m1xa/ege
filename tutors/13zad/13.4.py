from ipaddress import*
k = 0
net = ip_network('171.128.0.0/255.128.0.0',0)
for ip in net:
    b = format(int(ip),'32b')
    if b[:16].count('1') < b[16:].count('1'):
        k+=1
print(k)