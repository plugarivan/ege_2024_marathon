'''Текстовый файл 24-280.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита. Определите максимальное количество идущих подряд символов, среди которых каждая из гласных букв (A, E, I, O, U, Y) встречается не более восьми раз, а буквы V, X и Z не встречаются совсем.'''
s = open('24-280.txt').readline()
count = {let: 0 for let in 'AEIOUYVXZ'}
left = 0
result = []
for right, c in enumerate(s):
    for let in 'AEIOUYVXZ':
        if c == let:
            count[let] += 1
    while any(count[let] > 0 for let in 'VXZ') or any(count[let] > 8 for let in 'AEIOUY'):
        for let in 'AEIOUYVXZ':
            if s[left] == let:
                count[let] -= 1
        left += 1
    result.append(right - left + 1)
print(max(result))
