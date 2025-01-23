for a in range(0,1000):
    flag = True
    for x in range(0,300):
        for y in range(0,300):
            if ((3*x+y>a) and (y<x) and (x<30))==1:
                flag = False
    if flag == True:
        print(a)
        break