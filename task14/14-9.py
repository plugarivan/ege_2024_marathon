'''(А. Богданов) Операнды арифметического выражения записаны в системе счисления с основанием 17:
    12346x1717 + 7x17117
где x – неизвестная цифра из алфавита 17-ричной системы счисления. Определите наименьшее значение х, при котором значение данного арифметического выражения кратно 16. Для найденного значения х вычислите частное от деления значения арифметического выражения на 16 и укажите его в ответе в десятичной системе счисления. Основание системы счисления указывать не нужно.
'''
alph = '0123456789ABCDEFG'
for x in alph:
    f = int(f'12346{x}17', 17) + int(f'7{x}171', 17)
    if f % 16 == 0:
        print(f // 16)
        break
