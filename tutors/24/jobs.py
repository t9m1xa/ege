f = open('c:/Users/t9m1x/Downloads/24.txt').readline()

f = f.replace('AC','*')
f = f.replace('AB','*')
k, m = 0 , 0
for i in range(len(f)):
    if f[i] == "*":
        k+=1
        m = max(m,k)
    else:
        k=0
print(m)

