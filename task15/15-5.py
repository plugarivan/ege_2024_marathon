'''Обозначим через ДЕЛ(n, m) утверждение «натуральное число n делится без остатка на натуральное число m». Для какого наименьшего натурального числа А формула
(ДЕЛ(x, 175) → ¬ДЕЛ(x, 25)) ∨ (2x + A ≥ 1780)
тождественно истинна (то есть принимает значение 1 при любом натуральном значении переменной х)?
'''
def f(x):
    return ((x % 175 == 0) <= (x % 25 != 0)) or (2 * x + a >= 1780)


for a in range(1, 10000):
    if all(f(x) for x in range(1, 10000)):
        print(a)
        break