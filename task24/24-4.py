'''Текстовый файл 24-181.txt содержит строку из заглавных латинских букв и точек, всего не более 106 символов. Определите максимальное количество идущих подряд символов, среди которых не более трёх точек.'''
s = '.' + open('24-181.txt').readline() + '.'
kmax = 0
a = [i for i in range(len(s)) if s[i] == '.']
for i in range(len(a) - 4):
    kmax = max(kmax, a[i + 4] - a[i] - 1)
print(kmax)