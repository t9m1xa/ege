"""
Алгоритм вычисления значения функции F(n), где n – натуральное число, задан следующими соотношениями: 
F(n) = 1 при n = 1; 
F(n) = n × F(n − 1), если n > 1. 
Чему равно значение выражения 
(2 × F(2024) + F(2023)) / F(2022)? 
"""
#from sys import*
#setrecursionlimit(10000)
from functools import*
@lru_cache(None)
def f(n):
    if n ==1 : return 1
    if n>1 : return n * f(n-1)
for i in range(1,2025):
    f(i)
s = (2*f(2024)+f(2023))/f(2022)
print(s)