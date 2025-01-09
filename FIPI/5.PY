def f(n,c):
    if c>10: 
        return print('тыче ишак')
    else:
        s = ''
        while n>0:
            s = str(n%c) + s
            n = n//c
        return s
for n in range (1,1000):
    s = f(n,2)
    if s.count('1')%2 == 0:
        s = '10' + s
    else:
        s = '1' + s + '01'
    r = int(s,2)
    if r > 516:
        print(n,r)
        break