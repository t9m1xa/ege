f = open('c:/Users/t9m1x/Downloads/27_А.txt')
def d(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
def cntr(clast):
    maxi = 0
    centr = [0,0]
    for i in clast:
        k = 0
        for g in clast:
            if d(i,g)<2.1:
                k+=1
        if k>maxi:
            maxi = k 
            centr = i
        elif k == maxi:
            if d(i,[0,0])<d(centr,[0,0]):
                centr = i
    return centr

l1 = []
l2 = []
for m in f:
    x , y = [float(x) for x in m.split()] #x,y = map(float,s.split())
    if x>0:
        l1.append([x,y])
    else:
        l2.append([x,y])
c1 = cntr(l1)
c2 = cntr(l2)

print(int(abs((c1[0]+c2[0])*5000)),int(abs((c1[1]+c2[1])*5000)))