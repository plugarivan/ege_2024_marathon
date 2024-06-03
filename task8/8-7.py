'''Маша составляет коды из букв, входящих в слово ГЕРАСИМ. Каждая буква должна входить в код ровно один раз. Все возможные коды Маша записывает в алфавитном порядке и нумерует. Начало списка выглядит так:
1. АГЕИМРС
2. АГЕИМСР
3. АГЕИРМС
...
Какой код будет записан под номером 1899?
'''
from itertools import permutations

print([i for i in permutations(sorted('герасим'))][1898])
