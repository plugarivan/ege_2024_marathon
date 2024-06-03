'''(М. Ишимов) Сколько существует шестеричных трёхзначных чисел, содержащих в своей записи ровно одну цифру 5, при этом никакая чётная цифра не стоит рядом с цифрой 5?'''
from itertools import product
k = 0
for x in product('012345', repeat=3):
    numb = ''.join(x)
    if numb.count('5') == 1 and all(ch + '5' not in numb for ch in '024') and all('5' + ch not in numb for ch in '024')\
            and numb[0] != '0':
        k += 1
print(k)
