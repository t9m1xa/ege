m=[]
for n in range(1,100):
    s=bin(n)[2:]
    a=s.count('1')
    if a%4==0:
        s='10'+s
    else:
        s='11'+s
    if s[-1]=='1':
        s=s+'0'
    else:
        s=s+'1'
    r=int(s,2)
    if r<=250:
        m.append(n)
print(max(m))
        
    
