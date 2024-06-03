'''В системе счисления с основанием p выполняется равенство
    zxyx8 + xy729 = wzx42 .
Буквами x, y, z и w обозначены некоторые цифры из алфавита системы счисления с основанием p. Определите значение числа xyzwp и запишите это значение в десятичной системе счисления.
'''
def f(a, n):
    return sum(a[::-1][i] * n ** i for i in range(len(a)))


for p in range(10, 50):
    for x in range(p):
        for y in range(p):
            for z in range(p):
                for w in range(p):
                    if f([z, x, y, x, 8], p) + f([x, y, 7, 2, 9], p) == f([w, z, x, 4, 2], p):
                        print(f([x, y, z, w], p))
