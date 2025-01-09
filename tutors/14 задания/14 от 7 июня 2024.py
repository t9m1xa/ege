'''
for x in range(1,2031):
    n= 3**100 - x
    n1=''
    while n>0:
        n1=str(n%3)+n1
        n=n//3
    if n1.count('0')==5:
        print(x)
'''

for x in range(1,2031):
    n= 3**100 - x
    n1=0
    while n>0:
        if n%3==0:
            n1+=1
        n=n//3
    if n1==5:
        print(x)

        

        
