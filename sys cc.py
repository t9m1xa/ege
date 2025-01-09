def f(n,c):
    if c>10: 
        return print('тыче ишак')
    else:
        s = ''
        while n>0:
            s = str(n%c) + s
            n = n//c
        return s
print(f(22,9))
print(f(33323333,3))