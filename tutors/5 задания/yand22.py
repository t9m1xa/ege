def f(n):
    s = ''
    while n>0:
        s = str(n%5)+ s
        n = n//5
    return s
for n in range ( 1 , 1000 ):
    s = f(n)
    if n%25 == 0:
        s = s[-3:]+s
    else:
        q = n%25
        s = s + f(q)
    r = int(s,5)
    if r>10000:
        print (n,r)
        break