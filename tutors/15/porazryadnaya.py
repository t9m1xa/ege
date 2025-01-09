for a in range(1,100):
    flag=True
    for x in range(1,300):
        if (( x & 125 !=  1) or  ((x & 34 == 2) <= (x & a == 0)))==0:
                flag=False
    if flag==True:
        print(a)
        
