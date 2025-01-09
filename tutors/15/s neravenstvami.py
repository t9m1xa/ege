for a in range(1,100):
    flag=True
    for x in range(1,300):
        for y in range(1,300):
            if (((y + 2*x) != 99) or (y > a) or (x>a))==0:
                flag=False
    if flag==True:
        print(a)
        
