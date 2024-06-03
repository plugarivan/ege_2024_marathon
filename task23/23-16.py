'''У исполнителя Калькулятор имеются четыре команды, которые обозначены латинскими буквами:
A. Вычесть 1
B. Вычесть 5
C. Прибавить 7
D. Умножить на 2
Найдите количество существующих программ, для которых при исходном числе 9 результатом является число 84, и при этом траектория вычислений содержит число 60 и не содержит чисел, оканчивающихся на 3, а программа не содержит двух команд вычитания подряд.
'''
from functools import lru_cache

@lru_cache
def f(x, y, k, h60):
    if x > y + 5 or x % 10 == 3: return 0
    if x == y: return h60
    if x == 60: h60 = True
    if k == 1:
        return f(x + 7, y, 2, h60) + f(x * 2, y, 3, h60)
    else:
        return f(x - 1, y, 1, h60) + f(x - 5, y, 1, h60) + f(x + 7, y, 3, h60) + f(x * 2, y, 4, h60)


print(f(9, 84, 0, 0))