'''Укажите наибольшее целое значение А, при котором выражение
(4y + 3x ≠ 65) ∨ (x > A) ∨ (3y > A)
истинно для любых целых положительных значений x и y.
'''
def f(x, y):
    return (4 * y + 3 * x != 65) or (x > a) or (3 * y > a)


for a in range(1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
