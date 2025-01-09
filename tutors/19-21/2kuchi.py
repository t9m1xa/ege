def f(s1,s2,c,m):
    if s1+s2 >= 50: return c%2==m%2
    if c==m: return 0
    h = [f(s1+3,s2,c+1,m),f(s1,s2+3,c+1,m), f(s1*3,s2,c+1,m),f(s1,s2*3,c+1,m)]
    return any(h) if c%2!=m%2 else any(h)
for s2 in range(2,46):
    for m in range(1,5):
        if f(4,s2,0,m) == 1:
            print(m,s2)
            break