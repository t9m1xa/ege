'''
Сколько существует четырёхзначных чисел, записанных в восьмеричной системе счисления,
в записи которых ровно две одинаковые цифры, причём стоящие рядом ?
'''
from itertools import*
n=0
str='01234567'
for i in product(str,repeat=4):
    s=''.join(i)
    if ((s[0]==s[1] and s[1]!=s[2] and s[1]!=s[3] and s[2]!=s[3]) or (s[1]==s[2] and s[2]!=s[0] and s[2]!=s[3] and s[0]!=s[3]) or (s[2]==s[3] and s[2]!=s[1] and s[2]!=s[0] and s[0]!=s[1])) \
        and s[0]!='0':
    #if ((x1==x2 and x2!=x3 and x2!=x4 and x3!=x4) or (x2==x3 and x3!=x1 and x3!=x4 and x1!=x4) or (x3==x4 and x3!=x2 and x3!=x1 and x1!=x2))::
        n+=1
print(n)