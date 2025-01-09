f = open('c:/Users/t9m1x/Downloads/17 (5).txt')
s = [int(x) for x in f]
s1 = [x for x in s if x%1000==832]
d = max(s1)
m = []
for i in range(len(s)-2):
    a = s[i:i+3]
    a1 = [x for x in a if 1000<=x<=9999]
    a3 = [x for x in a if x % 3 == 0]
    a5 = [x for x in a if x % 5 == 0]
    if len(a1)>=1 and (3-len(a1) >= 1):
        if len(a3)< len(a5):
            if sum(a) > d :
                m.append(sum(a))
print(len(m), max(m))   
