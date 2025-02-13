from ipaddress import*

for a in range(0,255+1):
    net = ip_network(f'248.112.{a}.35/255.255.255.240',0)
    flag = True
    for ip in net:
        b = format(int(ip),'32b')
        if b[:16].count('0') > b[16:].count('0'):
            flag = False
            break
    if flag == True:
        print(a)
