'''*Определите количество семизначных чисел, записанных в девятеричной системе счисления, в записи которых ровно одна цифра 8 и ровно четыре нечётные цифры.'''
from itertools import product
#c - 0246
#n - 1357
k = 0
for w in product('cn8', repeat=7):
    w = ''.join(w)
    if w.count('n') == 4 and w.count('8') == 1:
        if w[0] == 'n' or w[0] == '8':
            k += 4 ** 4 * 4 ** 2
        else:
            k += 4 ** 4 * 4 * 3
print(k)
