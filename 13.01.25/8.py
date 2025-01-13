from itertools import*
n=0
m=[]
for i in product(sorted('СЕНТЯБРЬ'),repeat=5):
    s=''.join(i)
    n+=1
    if s[0] == 'Р' and 'Ь' not in s:
        m.append([s,n])
print(max(m))
