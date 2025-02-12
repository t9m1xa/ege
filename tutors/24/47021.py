f = open('c:/Users/t9m1x/Downloads/24 (5).txt').readline()
s = 'AJNIJBANBFGUAOKOKOKOKOKOKOKOKOKOKOKOKOKOABUINMOIMA'
s1 = f.split('A')
k = 0 
for x in s1:
    if len(x) >=8 and 'B' not in x:
        k+=1
print(k)
