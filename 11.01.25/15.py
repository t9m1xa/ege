b = [-42 , -10 , -8 , 2, 16]
c = [-10 , -4 , 2, 15, 23 ]
a = set()
for x in range(1000):
    if (((x in a) <= (x in b)) or (x in c)) == 0:
        print (x)