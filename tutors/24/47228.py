f = open('c:/Users/t9m1x/Downloads/24 (3).txt').readline()
f = f.replace('O','G')
f = f.replace('A','G')
f = f.replace('C','S')
f = f.replace('D','S')
f = f.replace('F','S')
f = f.replace('SG','*')
print(f[100:200])
k , m = 0,0
for i in range(len(f)):
    if f[i] == '*':
        k+=1
        m = max(k,m)
    else:
        k = 0 
print(m)
