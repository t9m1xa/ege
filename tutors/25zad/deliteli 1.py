'''Напишите программу, которая ищет среди целых чисел, 
принадлежащих числовому отрезку [174457; 174505], числа, имеющие ровно 
два различных натуральных делителя, не считая единицы и самого числа. 
Для каждого найденного числа запишите эти два делителя в два соседних столбца 
на экране с новой строки в порядке возрастания произведения этих двух делителей. 
Делители в строке также должны следовать в порядке возрастания.'''

for i in range (174457,174505+1):
    k = []
    for d in range(2,i//2+1):
        if i%d == 0:
            k.append(d)
    if len(k) == 2:
        print(*k)