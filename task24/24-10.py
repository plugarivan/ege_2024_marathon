'''Текстовый файл 24-212.txt содержит строку из набора A, B, C, D, O, всего не более чем из 106 символов. Определите максимальное количество идущих подряд пар символов вида «гласная + согласная».'''
s = open('24-212.txt').readline()
kmax = k = 0
i = 0
while i < len(s) - 1:
    if s[i] in 'AO' and s[i + 1] in 'BCD':
        k += 1
        kmax = max(k, kmax)
        i += 2
    else:
        k = 0
        i += 1
print(kmax)