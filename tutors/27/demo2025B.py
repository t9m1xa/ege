f = open('c:/Users/t9m1x/Downloads/27_B.txt')
def d(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
rm = 10**10000
l1 = []
l2 = []
l3 = []

for m in f:
    x , y = [float(x) for x in m.replace(',','.').split()] #x,y = map(float,s.split())
    if x>5:
        l1.append([x,y])
    elif y>4:
        l2.append([x,y])
    else:
        l3.append([x,y])

#print(l1[:10],l2[:10],l3[:10])
c1 = []
c2 = []
c3 = []
for i in range(len(l1)):
    dl = sum([d(l1[i],p) for p in l1])
    if dl < rm:
        rm = dl
        c1=[l1[i][0],l1[i][1]]
rm = 10**10000

for i in range(len(l2)):
    dl = sum([d(l2[i],p) for p in l2])
    if dl < rm:
        rm = dl
        c2=[l2[i][0],l2[i][1]]
rm = 10**10000

for i in range(len(l3)):
    dl = sum([d(l3[i],p) for p in l3])
    if dl < rm:
        rm = dl
        c3=[l3[i][0],l3[i][1]]
#print(c1)
print(int((c1[0]+c2[0]+c3[0])/3*10000),int((c1[1]+c2[1]+c3[1])/3*10000))        
