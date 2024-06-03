'''В файле 17-205.txt содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от –10 000 до 10 000 включительно. Определите количество пар, в которых хотя бы один из двух элементов заканчивается на 17, а их сумма делится на 2. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму элементов таких пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.'''
s = [int(i) for i in open('17-205.txt')]
res = []
for i in range(len(s) - 1):
    if (str(s[i])[-2:] == '17' or str(s[i + 1])[-2:] == '17') and (s[i] + s[i + 1]) % 2 == 0:
        res.append(s[i] + s[i + 1])
print(len(res), max(res))
