f = open('c:/Users/t9m1x/Downloads/17 (1).txt')
s = [int(x) for x in f]
m = []
for i in range(len(s)-1):
    for g in range(i+1,len(s)):
        if (s[i]*s[g]) % 10 == 0:
            m.append(s[i]+ s[g])
print(len(m) , max(m))