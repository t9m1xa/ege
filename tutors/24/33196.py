f = open('c:/Users/t9m1x/Downloads/24 (4).txt').readline()
s = ''
m = 0
for i in range(len(f)-1):
    if f[i] == 'A':
        s += f[i+1]
for x in s:
    if s.count(x) > m:
        m = s.count(x) 
        b = x
print(m,b)

