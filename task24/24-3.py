'''(В.Н. Шубинкин) Текстовый файл 24.txt состоит не более чем из 106 символов - заглавных латинских букв и цифр. Возрастающей подпоследовательностью будем называть непрерывную последовательность символов, расположенных в порядке увеличения их номера в кодовой таблице символов ASCII. Найдите наибольшую возрастающую подпоследовательность в этом файле, запишите в ответе сначала саму последовательность, а затем – её длину. Если таких последовательностей несколько, используйте первую из них.'''
s = open('24.txt').readline()
k = kmax = 1
for i in range(1, len(s)):
    if s[i] > s[i - 1]:
        k += 1
        if k > kmax:
            kmax = k
            pos = i
    else:
        k = 1
print(s[pos - kmax + 1:pos + 1], kmax)
