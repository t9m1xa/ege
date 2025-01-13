a = 4**644 + 4**322 + 16**35 - 64**3
def f(n):
    s = ''
    while n>0:
        s = str(n%4) + s
        n= n//4
    return s
print(f(a),f(a).count('3'))