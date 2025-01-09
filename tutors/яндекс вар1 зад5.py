for n in range(26,100):
    s=bin(n)[2:]
    if n%2!=0:
        s=s[-2:]+"10"
    else:
        s="10"+s[2:]+"1"
    r=int(s,2)
    print(r)
    break
