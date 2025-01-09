'''
Сколько существует чисел, восьмеричная запись которых содержит 7 цифр,
 причём все цифры различны и никакие две чётные и две нечётные цифры не стоят рядом.
'''
from itertools import*
n=0
str='01234567'
for i in product(str,repeat=7):
    s=''.join(i)
    if s[0]!='0' and s.count('0')<=1 and s.count('1')<=1 and s.count('2')<=1 and s.count('3')<=1 and s.count('4')<=1 and s.count('5')<=1 and s.count('6')<=1 and s.count('7')<=1:
        s=s.replace('0','2').replace('4','2').replace('6','2').replace('3','1').replace('5','1').replace('7','1')
        if '22' not in s and '11' not in s:
            n+=1
print(n)