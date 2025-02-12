def be(a, b, c):
    x, y = sorted([a, b, c])[-2:] 
    return int(f"{x}{y}")

for i in range(1000,9999+1):
    s = str(i)
    a = int(s[0])*int(s[1])
    b = int(s[0])*int(s[2])
    c = int(s[0])*int(s[3])
    la = be(a,b,c)
    if la == 5472:
        print(i)
        break