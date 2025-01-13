for i in range(1,1000):
    n = str(bin(i)[2:])
    if n.count('1')%2 == 0:
        n = n+ '11'
    else:
        n = n + '01'
    r = int(n,2)
    if r>61:
        print(r,n)
        break