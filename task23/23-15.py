'''У исполнителя Калькулятор имеются три команды, которые обозначены латинскими буквами:
A. Вычесть 1
B. Прибавить 2
C. Умножить на 3
Найдите количество существующих программ, для которых при исходном числе 5 результатом является число 62, и при этом траектория вычислений содержит число 32 и не содержит чисел, оканчивающихся на 0, а программа не содержит двух команд вычитания подряд.
'''
from functools import lru_cache

@lru_cache
def f(x, y, k, h32):
    if x > y+1 or x % 10 == 0: return 0
    if x == y: return h32
    if x == 32: h32 = True
    if k == 1:
        return f(x + 2, y, 2, h32) + f(x * 3, y, 3, h32)
    else:
        return f(x - 1, y, 1, h32) + f(x + 2, y, 2, h32) + f(x * 3, y, 3, h32)


print(f(5, 62, 0, 0))
