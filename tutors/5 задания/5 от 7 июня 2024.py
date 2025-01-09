for n in range(1,100):
    
    s=bin(n)[2:]
    if s.count('1')%2==0:
        s=s+'0'
        s='10'+s[2:]
    else:
        s=s+'1'
        s='11'+s[2:]
    r=int(s,2)
    if r>50:
        print(n)
        break


















































































        
