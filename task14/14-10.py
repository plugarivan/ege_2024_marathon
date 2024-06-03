'''Операнды арифметического выражения записаны в системе счисления с основанием 19.
    78x7964319 +25x4319+63x519
В записи чисел переменной x обозначена неизвестная цифра из алфавита 19-ричной системы счисления. Определите наименьшее значение x, при котором значение данного арифметического выражения кратно 18. Для найденного x вычислите частное от деления значения арифметического выражения на 18 и укажите его в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.
'''
alph = '0123456789ABCDEFGHI'
for x in alph:
    f = int(f'78{x}79643', 19) + int(f'25{x}43', 19) + int(f'63{x}5', 19)
    if f % 18 == 0:
        print(f // 18)
        break
