m=[]
for n in range(1,100):
    n1=n-bin(n)[2:].count('0')
    s=bin(n1)[2:]
    s=s[-3:]+s
    r=int(s,2)
    if r>224:
        m.append(r)
print(min(m))
        
    
