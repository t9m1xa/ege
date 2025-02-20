f = open('c:/Users/t9m1x/Downloads/banf.txt')
s = f.readline()
'''s = s.replace('BB','B B').replace('BB','B B').replace('AB','A B')
s = s.replace('CB','C B').replace('BC','B C').replace('BA','B A')
s = s.split()'''
s = s.replace('AA','*').replace('CC','*')
m=0
k=1
for i in range(len(s)-1):
    #b = s[i+2:s+3]
    if s[i] == '*' and s[i+1] == '*':
        k+=1
        m= max(k,m)
    else:
        k = 1
print(m)
