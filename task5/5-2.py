'''(А. Игнатюк) Исполнитель «Аполлон» получает на вход четырёхзначное число N и строит новое число R по следующим правилам:
1) Если число N начинается с чётной цифры, то число R вычисляется как сумма первой и третьей цифр и модуля разности второй и четвёртой цифр.
2) Если число N начинается с нечётной цифры, то цифры числа N располагают в неубывающем порядке. Число R вычисляется как сумма цифр в двоичной записи полученного числа.
Сколько существует чисел N, для которых результат работы алгоритма будет более 20?
'''
k = 0
for n in range(1000, 10000):
    s = str(n)
    if int(s[0]) % 2 == 0: res = (int(s[0]) + int(s[2])) + abs(int(s[1]) - int(s[3]))
    else: res = bin(int(''.join(sorted(s))[2:])).count('1')
    if res > 20:
        k += 1
print(k)
