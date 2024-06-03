'''Назовём маской числа последовательность цифр, в которой также могут встречаться следующие символы:
— символ «?» означает ровно одну произвольную цифру;
— символ «*» означает любую последовательность цифр произвольной длины; в том числе «*» может задавать и пустую последовательность.
Среди натуральных чисел, не превышающих 108, найдите все числа, соответствующие маске 1234*7, делящиеся на 141 без остатка. В ответе запишите в первом столбце таблицы все найденные числа в порядке возрастания, а во втором столбце – соответствующие им результаты деления этих чисел на 141.
'''
from fnmatch import fnmatch

for n in range(0, 10 ** 8 + 1, 141):
    if fnmatch(str(n), '1234*7'):
        print(n, n // 141)
