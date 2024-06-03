'''Алгоритм вычисления значений функций F(n) и G(n), где n – натуральное число, задан следующими соотношениями:
F(1) = 1; G(1) = 1;
F(n) = F(n–1) + 3·G(n–1), при n >=2
G(n) = F(n–1) - 2·G(n–1), при n >=2
Чему равна сумма цифр значения F(18)?
'''
def f(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) + 3 * g(n - 1)


def g(n):
    if n == 1: return 1
    if n >= 2: return f(n - 1) - 2 * g(n - 1)


print(sum(map(int, str(f(18)))))
