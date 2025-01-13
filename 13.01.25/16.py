def f(n):
    if n>400: return n**n
    else: return n+6+f(n+12)
a = f(72) - f(108)
print(a)