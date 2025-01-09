f = open('c:/Users/t9m1x/Downloads/17 (2).txt')
s = [int(x) for x in f]
s1 = [x for x in s if abs(x) % 32 == 0]
d = len(s1)
m = []
for i in range(len(s)-1):
    if (s[i]<0 or s [i+1]<0) and (s[i] + s[i+1])<d:
        m.append(s[i]+s[i+1])
print(s)   
f = open('c:/Users/t9m1x/Downloads/17 (2).txt')
a = [int(x) for x in f]
count_delit_32 = 0
for i in range(len(a)):
    if a[i]%32==0:
        count_delit_32 += 1
answer = []
for j in range(len(a)-1):
    if (a[j] < 0 or a[j+1] <0) and ((a[j] + a[j+1]) < count_delit_32):
        answer.append(a[j] + a[j+1])
print(len(answer),max(answer))