from functools import*
@lru_cache(None)
def f(n):
    if n<=10: return n*2
    if n%2 == 0 and n>10: return f(n-3)- f(n-9)*2
    if n%2!=0 and n>10: return f(n-2)*2 - f(n-7)
for i in range(3063):
    f(i)
s = str(f(3063))
m=0
for i in s:
    m+=int(i)
print(m)
