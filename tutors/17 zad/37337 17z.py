f = open('17.txt')
s = [int(x) for x in f]
m = []
for i in range (len(s)-1):
    for g in range(i+1, len (s)):
        if s[i] % 160 != s[g] % 160 and ( s[i]%7 == 0 or s[g] % 7 == 0):
            m.append(s[i]+s[g])
print(len(m),max(m))


