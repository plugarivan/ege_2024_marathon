'''В файле 17-370.txt содержится последовательность целых чисел, по модулю не превышающих 20000. Определите количество пар элементов последовательности, в которых
– только одно число четырёхзначное;
– сумма квадратов элементов пары делится нацело на максимальное трёхзначное число в последовательности, троичная запись которого является палиндромом.
В ответе запишите сначала количество найденных пар, затем минимальную из сумм квадратов элементов таких пар. Под парой элементов подразумеваются два соседних элемента последовательности.
'''
def pal(a):
    a_r = ''
    while a:
        a_r += str(a % 3)
        a //= 3
    return a_r == a_r[::-1]


s = [int(i) for i in open('17-370.txt')]
res = []
max3 = max(t for t in s if pal(abs(t)) and 100 <= abs(t) <= 999)
for i in range(len(s) - 1):
    if ((1000 <= abs(s[i]) <= 9999) + (1000 <= abs(s[i + 1]) <= 9999)) == 1 and \
                (s[i] ** 2 + s[i + 1] ** 2) % max3 == 0:
        res.append(s[i] ** 2 + s[i + 1] ** 2)
print(len(res), min(res))