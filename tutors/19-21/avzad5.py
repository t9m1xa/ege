def f ( s1, s2 , c , m ):
    if s1+s2>=57: return c % 2 == m % 2
    if c == m : return 0
    h = [ f(s1+s2,s2,c+1,m) , f(s1,s1+s2,c+1,m) ]
    return any (h) if c%2!=m%2 else any (h)
for s2 in range (1,57-9+1):
    for m in range (1,10):
        if f( 10 , s2, 0 , m) == 1:
            print(s2 , m)
            break