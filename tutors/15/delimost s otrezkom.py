A=[]
for a in range(1,100):
    flag=True
    for x in range(1,300):
        if (a or ((10<=x<=40) <= (x%6 != 0))) ==1:
                flag=False
    if flag==True:
        A.append(a)
print(A)
        
