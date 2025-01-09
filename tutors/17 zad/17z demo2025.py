f = open('c:/Users/t9m1x/Downloads/demo_2025_17.txt')
s = [int(x) for x in f]
g = min(s)
m = []
for i in range(len(s)-1):
    if s[i] % 16 == g or s[i+1] % 16 == g:
        m.append(s[i]+s[i+1])
print(len(m), max(m))
    