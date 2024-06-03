'''*Добрыня составляет коды из букв, входящих в слово ДОБРЫНЯ. Код должен состоять из 6 букв, буквы в коде не должны повторяться, согласных в коде должно быть больше, чем гласных, две гласные буквы нельзя ставить рядом. Сколько различных кодов может составить Добрыня?'''
from itertools import permutations
k = 0
for w in permutations('добрыня', r=6):
    s = ''
    for c in w:
        if c in 'дбрн': s += 's'
        else: s += 'g'
    if s.count('s') > s.count('g') and 'gg' not in s:
        k += 1
print(k)
