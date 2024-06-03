'''Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА нашлось (63) ИЛИ нашлось (664) ИЛИ нашлось (6665)
  ЕСЛИ нашлось (63) ТО заменить (63, 4)
  ИНАЧЕ
    ЕСЛИ нашлось (664) ТО заменить (664, 65)
    ИНАЧЕ
      ЕСЛИ нашлось (6665) ТО заменить (6665, 63) КОНЕЦ ЕСЛИ
    КОНЕЦ ЕСЛИ
  КОНЕЦ ЕСЛИ
КОНЕЦ ПОКА
КОНЕЦ
Какая строка получится в результате применения приведённой выше программы к строке, в которой первая и последняя цифры – 3, а между ними стоит 115 цифр 6? В ответе запишите полученную строку.
'''
s = '3' + 115 * '6' + '3'
while '63' in s or '664' in s or '6665' in s:
    if '63' in s: s = s.replace('63', '4', 1)
    elif '664' in s: s = s.replace('664', '65', 1)
    elif '6665' in s: s = s.replace('6665', '63', 1)
print(s)
