
f = open('c:/Users/t9m1x/Downloads/24 (11).txt')
s = f.readline()

m = 0

for i in range(len(s)-4) :
    l = s[i:i+5]
    l1 = l[::-1]
    
    
    if l1 == l:
        m+=1
print(m)

