'''(А. Кабанов) В файле 17-4.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 0 до 10 000 включительно. Рассматривается множество элементов последовательности, которые удовлетворяют следующим условиям:
− остаток от деления на 13 равен 4;
− остаток от деления на 8 равен 1.
Найдите наибольшее из таких чисел и их сумму. Гарантируется, что искомая сумма не превосходит 107.
'''
s = [int(i) for i in open('17-4.txt')]
res = []
for i in s:
    if i % 13 == 4 and i % 8 == 1:
        res.append(i)
print(max(res), sum(res))