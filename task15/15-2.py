'''Укажите наименьшее целое значение А, при котором выражение
(xy < 2A) ∨ (x ≥ 19) ∨ (x < 6y)
истинно для любых целых положительных значений x и y.
'''
def f(x, y):
    return (x * y < 2 * a) or (x >= 19) or (x < 6 * y)


for a in range(1000):
    if all(f(x, y) for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
        break
