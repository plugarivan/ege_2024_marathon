'''Текстовый файл 24-157.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита (ABC…Z). Определите символ, который чаще всего встречается в файле между двумя одинаковыми символами. Например, в тексте CCBAABABCBC есть комбинации ABA, BAB, BCB и CBC. Чаще всего – 2 раза – между двумя одинаковыми символами стоит B, в ответе для этого случая надо написать B2 (без пробелов и других разделителей). Если таких символов несколько, выведите тот, который стоит раньше в алфавите.'''
s = open('24-157.txt').readline()
d = {}
for i in range(len(s) - 2):
    if s[i] == s[i + 2]:
        key = s[i + 1]
        d[key] = d.get(key, 0) + 1
for x in d.items():
    if x[1] == max(d.values()):
        print(x)