for a in range(-100,100):
    flag=True
    for k in range(1,300):
        for n in range(1,300):
            if ((5*k+6*n>57) or ((k<=a) and (n<a)))==0:
                flag=False
    if flag==True:
        print(a)
        
