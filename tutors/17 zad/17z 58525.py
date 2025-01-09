f = open('C:/Users/t9m1x/Downloads/17 (6).txt')
s = [int(x) for x in f]
s1 = [x for x in s if 100<=x<=999 and x%10 == 3]
d = min(s1)
m = []
for i in range(len(s)-1):
        if (1000<=s[i]<=9999 and not(1000<=s[i+1]<=9999)) or (1000<=s[i+1]<=9999 and not(1000<=s[i]<=9999)):
            if (s[i]**2 + s[i+1]**2)% d == 0:
                m.append(s[i]**2 + s[i+1]**2)
print(len(m),max(m))