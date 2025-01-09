from itertools import*
k = 0
for i in product(sorted('ЯНВАРЬ'),repeat=5):
    s = ''.join(i)
    k+=1
    if s[0] != 'Я' and s.count('Ь') <= 1 and 'ЯЯ' not in s:
        print(k,s)
