'''(PRO100 ЕГЭ) Два игрока, Петя и Ваня, играют в следующую игру. Перед игроками лежит куча камней. Игроки ходят по очереди, первый ход делает Петя. За один ход игрок может добавить в кучу один камень или три камня или одиннадцать камней. Для того чтобы делать ходы, у каждого игрока есть неограниченное количество камней.
Игра завершается в тот момент, когда количество камней в куче становится числом, оканчивающимся на ноль. Победителем считается игрок, сделавший последний ход, т.е. первым получивший кучу, количество камней в которой оканчивается на ноль. К примеру, игра заканчивается, когда в куче стало 10, 200, 6800 камней. В начальный момент в куче было S камней, где S – двузначное число, не оканчивающиеся на ноль.
Ответьте на следующие вопросы:
  Вопрос 1. Укажите минимальное значение S, при котором Петя не может выиграть за один ход, но при любом ходе Пети Ваня может выиграть своим первым ходом.
  Вопрос 2. Найдите количество значений S, при которых у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
– Петя не может выиграть за один ход;
– Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.
  Вопрос 3. Найдите сумму значений S, при которых у Вани есть выигрышная стратегия, причём одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''
def f(x, p):
    if x % 10 == 0 or p > 2:
        return p == 2
    if p % 2:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x + 11, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x + 11, p + 1)


print(min([s for s in range(10, 100) if f(s, 0) and s % 10 != 0]))

def f(x, p):
    if x % 10 == 0 or p > 3:
        return p == 3
    if p % 2 == 0:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x + 11, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x + 11, p + 1)


print(len([s for s in range(10, 100) if f(s, 0) and s % 10 != 0]))

def f(x, p):
    if x % 10 == 0 or p > 4:
        return p == 2 or p == 4
    if p % 2:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x + 11, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x + 11, p + 1)


print(sum([s for s in range(10, 100) if f(s, 0) and s % 10 != 0]))

def f(x, p):
    if x % 10 == 0 or p > 2:
        return p == 2
    if p % 2:
        return f(x + 1, p + 1) or f(x + 3, p + 1) or f(x + 11, p + 1)
    else:
        return f(x + 1, p + 1) and f(x + 3, p + 1) and f(x + 11, p + 1)


print(sum([s for s in range(10, 100) if f(s, 0) and s % 10 != 0]))
