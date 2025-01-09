m = set()
def f(n,k=0):
    if k==15:
        m.add(n)
        return 0 
    return f(n+5,k+1) + f(n*2,k+1)
f(155)
print(len(m))
        