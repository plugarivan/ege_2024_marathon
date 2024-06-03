'''Автомат обрабатывает натуральное число N < 256 по следующему алгоритму:
1) Строится восьмибитная двоичная запись числа N.
2) Инвертируются все разряды исходного числа, кроме последней единицы и стоящих за ней нулей (0 заменяется на 1, 1 на 0).
3) Полученное число переводится в десятичную систему счисления.
Для какого значения N результат работы алгоритма равен 11?
'''
for n in range(1, 256):
    s = bin(n)[2:].zfill(8)
    s1 = ''
    i1 = s.rindex('1')
    for i in range(i1):
        if s[i] == '1': s1 += '0'
        else: s1 += '1'
    s1 += s[i1:]
    if int(s1, 2) == 11:
        print(n)
