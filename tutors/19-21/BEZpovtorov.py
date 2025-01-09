# +1 , +2 , *2, нельзя повторять ход ,  s>= 68

def f ( s , c , m , p ):
    if s>=68 : return c % 2 == m%2
    if c == m : return 0 
    h = []
    if p != '+1' : h+=[f(s+1,c+1,m,'+1')]
    if p != '+2' : h+=[f(s+2,c+1,m,'+2')]
    if p != '*2' : h+=[f(s*2,c+1,m,'*2')]
    return any ( h ) if c%2 != m%2 else all (h) 
for s in range (1,68):
    for m in range ( 1 , 6):
        if f(s,0,m,'') == 1:
            print ( s , m )
            break
