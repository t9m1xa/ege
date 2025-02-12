f = open("c:/Users/t9m1x/Downloads/inf_22_10_20_24.txt")
s = [x for x in f]
k=0
for n in s:
    if n.count('E') > n.count('A'):
        k+=1
print(k)