def f(x,y):
    if x == y: return 1

    if x>y or x == 22: return 0

    if x<y: return f(x+3,y) + f(x+4,y)
print(f(16,38))