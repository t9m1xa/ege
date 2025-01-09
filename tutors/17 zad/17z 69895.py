f = open('c:/Users/t9m1x/Downloads/17 (4).txt')
s = [int(x) for x in f]
s1 = [x for x in s if x%1000==562]
d = max(s1)
m = []
for i in range(len(s)-3):
    a = s[i:i+4]
    a1 = [x for x in a if 10000<=x<=99999]
    a3 = [x for x in a if x % 3 == 0]
    a7 = [x for x in a if x % 7 == 0]
    if len(a1)>=1 and (4-len(a1) >= 2):
        if len(a3)< len(a7):
            if sum(a) > d and sum(a)< 2*d:
                m.append(sum(a))
print(len(m), max(m))   
