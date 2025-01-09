for a in range(1,100):
    flag = True
    for x in range(1,300):
        for y in range(1,300):
            if (((y+x)**2 > 1048) or (((x+20)<a) and ((40 - y) < a))) ==0:
                flag = False
    if flag == True:
        print(a)
        break
    
