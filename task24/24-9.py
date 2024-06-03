'''Текстовый файл 24-210.txt содержит строку из набора A, B, C, D, E, F, всего не более чем из 106 символов. Найдите максимальное количество подряд идущих троек символов ABC, BAC, CAB, CBA, стоящих одна за другой и пересекающихся с соседними тройками одной буквой. Например, в строке BDEABCBABCABBD такие пары составляют подстроку ABCBABCAB = ABC + СBA + ABC + CAB, итого 4 тройки.'''
s = open('24-210.txt').readline()
kmax = k = 0
i = 0
while i < len(s) - 2:
    if s[i:i+3] in ['ABC', 'BAC', 'CAB', 'CBA']:
        k += 1
        kmax = max(k, kmax)
        i += 1
    else:
        k = 0
    i += 1
print(kmax)