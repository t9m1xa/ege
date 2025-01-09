for x in range(1,2031):
    n=7**91+7**160 - x
    n1=0
    while n>0:
        if n%7==0:
            n1+=1
        n=n//7
    if n1==70:
        print(x)
