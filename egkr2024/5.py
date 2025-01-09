def f(n):
    s = ''
    while n>0:
        s = str(n%3) + s
        n = n//3
    return s
m = []
for n in range(1,1000):
    s = f(n)
    if n%3 == 0:
        s = s + s[-2:]
    else:
        a = s.count('1')+s.count('2')*2
        a1 = f(a)
        s = s+ a1
    r = int(s,3)
    if r>220 and r%2 == 0:
        m.append(r)
print(min(m))