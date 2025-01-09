'''Среди натуральных чисел, не превышающих 10**10, 
найдите все числа, соответствующие маске 1?2139*4, делящиеся на 2023 без остатка.
В ответе запишите в первом столбце таблицы все найденные 
числа в порядке возрастания, а во втором столбце – соответствующие 
им результаты деления этих чисел на 2023.
'''
from fnmatch import *
for i in range(2023,10**10,2023):
    if fnmatch(str(i),'1?2139*4'):
        print(i,i//2023)