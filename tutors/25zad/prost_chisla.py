'''Напишите программу,
которая ищет среди целых чисел, принадлежащих числовому 
отрезку [2422000; 2422080], простые числа. 
Выведите все найденные простые числа в порядке возрастания,
 слева от каждого числа выведите его номер по порядку.'''
a = 0
for i in range (2422000,2422080+1):
    k = []
    a+=1
    for d in range(2,i//2+1):
        if i%d == 0:
            k.append(d)

    if len(k) == 0:
        
        print(a,i)