'''Текстовый файл 24-280.txt состоит не более чем из 106 символов и содержит только заглавные буквы латинского алфавита. Определите максимальное количество идущих подряд символов, среди которых каждая из букв X, Y, Z встречается не более трёх раз.'''
s = open('24-280.txt').readline()
left = 0 #граница левая
result = []
letters = {x: 0 for x in 'XYZ'}
#сдвигает правую границу
for right in range(len(s)):
    if s[right] in 'XYZ':
        letters[s[right]] += 1
    #сдвиг левой границы
    while all(letters[x] <= 3 for x in 'XYZ') == 0:
        if s[left] in 'XYZ':
            letters[s[left]] -= 1
        left += 1
    result.append(right - left + 1)
print(max(result))
