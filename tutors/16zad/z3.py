def f(n):
    #print(2*n)
    global s
    s+=2*n
    if n > 1:
        #print(n-5)
        s+=n-5
        f(n-1)
        f(n-2)

for n in range(1,100):
    s = 0
    f(n)
    if s > 500000:
        print(n, s)
        break

