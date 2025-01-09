m=[]
for x in range(16):
    for y in range(16):
        n1=2*16**5+7*16**4+10*16**3+x*16**2+2*16+3
        n2=8*16**5+y*16**4+14*16**3+5*16**2+13*16+2
        n=n1+n2
        if n%5==0:
            m.append(x+y)
print(max(m))
