def f(s,c,m):
    if s >= 61: return c%2==m%2
    if c==m: return 0
    h = [f(s+3,c+1,m),f(s+10,c+1,m), f(s*2,c+1,m)]
    return any(h) if c%2!=m%2 else any(h)
for s in range(1,61):
    for m in range(1,5):
        if f(s,0,m) == 1:
            print(m,s)
            break