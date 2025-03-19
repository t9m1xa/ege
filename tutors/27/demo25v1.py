f = open('c:/Users/t9m1x/Downloads/27_A.txt')
def d(a,b):
    return ((a[0]-b[0])**2+(a[1]-b[1])**2)**0.5
def cntr(clast):
    rm = 10**10
    maxi = 0
    centr = [0,0]
    for i in clast:
        dl = sum([d(i,p) for p in clast])
        if dl<rm:
            rm = dl
            centr = i
    return centr

l1 = []
l2 = []

for m in f:
    x , y = [float(x) for x in m.split()] #x,y = map(float,s.split())
    if x>1:
        l1.append([x,y])
    else:
        l2.append([x,y])
c1 = cntr(l1)
c2 = cntr(l2)


print(int(abs((c1[0]+c2[0])*10000/2)),int(abs((c1[1]+c2[1])*10000/2)))