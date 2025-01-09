from fnmatch import*
k = 0
for i in range (10**6,10**5,-1):
    
    for d in range(2,i+1):
        if i%d == 0 :
            if fnmatch(str(d),'1??56*5'):
                k+=1
                if k<=5:
                    print(i,d)
                else:
                    break


