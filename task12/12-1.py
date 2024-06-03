'''Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (33333) ИЛИ нашлось (999)
  ЕСЛИ нашлось (33333)
    ТО заменить (33333, 99)
    ИНАЧЕ заменить (999, 3)
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой ниже программы к строке, состоящей из 84 идущих подряд цифр 9?
'''
s = 84 * '9'
while '33333' in s or '999' in s:
    if '33333' in s: s = s.replace('33333', '99', 1)
    else: s = s.replace('999', '3', 1)
print(s)
