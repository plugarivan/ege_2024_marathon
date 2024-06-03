'''Исполнитель Калькулятор преобразует число, записанное на экране в троичной системе счисления. У исполнителя есть две команды, которым присвоены номера:
1. Прибавь 2
2. Умножь на 2 и прибавь 1
Сколько различных результатов можно получить из исходного числа 2 после выполнения программы, содержащей ровно 15 команд?
'''
def f(x, k):
    if k == 15:
        s.add(x)
    else:
        f(x + 2, k + 1)
        f(x * 2 + 1, k + 1)


s = set()
f(2, 0)
print(len(s))
