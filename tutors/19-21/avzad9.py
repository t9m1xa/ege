def f ( s , c , m):
    if s <= 0 : return c%2 == m%2
    if c == m : return 0
    h = [ f(s-5, c + 1 , m) , f(s//3,c+1, m) ]
    return any (h) if c%2 != m%2 else all (h)
for s in range (1,50):
    for m in range(1,5):
        if f(s, 0 ,m) == 1:
            print(s,m)
            break