'''Число 804 записали в системах счисления с основаниями от 2 до 10 включительно. При каких основаниях в записи этого числа есть цифра 1? В ответе укажите сумму всех подходящих оснований.'''
summ = 0
for n in range(2, 11):
    x = 804
    s = ''
    while x > 0:
        s = str(x % n) + s
        x //= n
    if '1' in s:
        summ += n
print(summ)
