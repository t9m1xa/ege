f = open('C:/Users/t9m1x/Downloads/lott.txt')
s = [int(x) for x in f]
m = []
for i in range(len(s)-6):
    if s[i+2]+s[i+3]>s[i+1]+s[i] and s[i+2]+s[i+3]>s[i+4]+s[i+5]:
        if s[i+2]+s[i+3]>0 and s[i+1]+s[i]>0 and s[i+4]+s[i+5]>0:
            m.append(s[i+2]*s[i+3])
print(len(m),min(m))
