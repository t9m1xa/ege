def f(s1,s2,c,m):
    if s1+s2>=100: return c%2 == m%2
    if c == m : return 0 
    h = [f(s1+3,s2,c+1,m), f(s1*2,s2,c+1,m) , f(s1,s2+3, c+1 ,m) , f(s1,s2*2,c+1,m)]
    return any (h) if c%2!=m%2 else all (h)
for m in range(1,10):
    if f(27,27,0,m) == 1:
        print (m)