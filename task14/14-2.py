'''Значение арифметического выражения
3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4
записали в системе счисления с основанием 25. Сколько значащих нулей содержится в этой записи?
'''
x = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2024
k = 0
while x:
    if x % 25 == 0: k += 1
    x //= 25
print(k)
