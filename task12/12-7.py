'''Дана программа для исполнителя Редактор:

НАЧАЛО
ПОКА НЕ нашлось(00)
  заменить(01, 21022)
  заменить(02, 310)
  заменить(03, 230112)
КОНЕЦ ПОКА
КОНЕЦ
Известно, что исходная строка начиналась с нуля и заканчивалась нулём, а между ними были только цифры 1, 2 и 3. После выполнения данной программы получилась строка, содержащая 96 единиц, 36 двоек и 80 троек. Сколько цифр было в исходной строке?
'''
for a in range(30):
    for b in range(30):
        for c in range(30):
            s = '0' + a * '1' + b * '2' + c * '3' + '0'
            while '00' not in s:
                s = s.replace('01', '21022', 1)
                s = s.replace('02', '310', 1)
                s = s.replace('03', '230112', 1)
            if s.count('1') == 96 and s.count('2') == 36 and s.count('3') == 80:
                print(a + b + c + 2)
