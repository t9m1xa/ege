"""
Алгоритм вычисления функции F(n), где n – натуральное число, задан следующими соотношениями:
F(n) = 1, если n = 1
F(n) = n · F(n – 1) + 1, если n > 1.
Чему равно значение выражения F(3303) / F(3300)? В ответе укажите только целую часть числа.
"""
#from sys import*
#setrecursionlimit(10000)
from functools import*
@lru_cache(None)
def F(n):
    if n==1: return 1
    if n > 1: return n * F(n-1) + 1
for i in range(1,3304):
    F(i)
s = F(3303) / F(3300)
print(s)