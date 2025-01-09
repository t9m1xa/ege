f = open('c:/Users/t9m1x/Downloads/17_2024.txt')
s = [int(x) for x in f]
s1 = [x for x in s if x%100== 13]
d = max(s1)
m = []
for i in range(len(s)-2):
    a = s[i:i+3]
    a1 = [x for x in a if 100<=x<=999]
    if len(a1) == 2 :
        if sum(a) <= d :
            m.append(sum(a))
print(len(m), max(m))   
