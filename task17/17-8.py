'''В файле 17-390.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –100 000 до 100 000 включительно. Определите количество троек, для которых выполняются следующие условия:
– в тройке есть пятизначные числа, но не все числа пятизначные;
– в тройке больше чисел, кратных 5, чем чисел, кратных 11;
– каждый элемент тройки больше среднего арифметического всех элементов последовательности, запись которых заканчивается на 641. (Гарантируется, что в последовательности есть хотя бы один элемент, запись которого заканчивается на 641.) В ответе запишите количество найденных троек, затем – минимальную из сумм элементов таких троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.
'''
s = [int(i) for i in open('17-390.txt')]
res = []
s641 = [i for i in s if str(i)[-3:] == '641']
sred = sum(s641) / len(s641)
for i in range(len(s) - 2):
    if 1 <= len([t for t in s[i:i+3] if 10000 <= abs(t) <= 99999]) < 3 and \
            len([t for t in s[i:i + 3] if t % 5 == 0]) > len([t for t in s[i:i + 3] if t % 11 == 0]) and \
            len([t for t in s[i:i + 3] if t > sred]) == 3:
        res.append(sum(s[i:i + 3]))
print(len(res), min(res))
