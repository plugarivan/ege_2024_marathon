'''Дана программа для исполнителя Редактор:

НАЧАЛО
  ПОКА нашлось (13) ИЛИ нашлось (32) ИЛИ нашлось (12)
    ЕСЛИ нашлось (13)
      ТО заменить (13, 31)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (32)
      ТО заменить (32, 23)
    КОНЕЦ ЕСЛИ
    ЕСЛИ нашлось (12)
      ТО заменить (12, 21)
    КОНЕЦ ЕСЛИ
  КОНЕЦ ПОКА
КОНЕЦ
На вход приведённой ниже программе поступает строка, содержащая 50 цифр 1, 50 цифр 2 и 50 цифр 3, расположенных в произвольном порядке. Запишите без разделителей символы, которые имеют порядковые номера 10, 70 и 140 в получившейся строке.
'''
s = 50 * '1' + 50 * '2' + 50 * '3'
while '13' in s or '32' in s or '12' in s:
    if '13' in s: s = s.replace('13', '31', 1)
    if '32' in s: s = s.replace('32', '23', 1)
    if '12' in s: s = s.replace('12', '21', 1)
print(s[9] + s[69] + s[139])
