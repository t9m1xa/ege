f = open('C:/Users/t9m1x/Downloads/17.txt')
s = [int(x) for x in f]
m = []
for i in range(len(s)-1):
    for g in range(i+1,len(s)):
        if abs(s[i] - s[g]) % 2 == 0 and (s[i]%31 == 0 or s[g]%31 == 0):
            m.append(s[i]+s[g])
print(len(m),max(m))