def f(n):
    if n <= 1 : return 1
    else: return (n+1)*f(n-1)
a = f(200)/f(198)
print(a)