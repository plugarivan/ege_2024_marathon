'''Исполнитель преобразует число, записанное на экране. У исполнителя есть две команды, которым присвоены номера:
1. Прибавь 2
2. Припиши 2
Первая команда увеличивает число на экране на 2, вторая приписывает 2 в конец десятичной записи числа. Программа для исполнителя – это последовательность команд. Например, если в начальный момент на экране находится число 1, то программа 212 последовательно преобразует его в 12, 14, 142. Сколько существует различных программ, которые преобразуют исходное число 2 в число 900?
'''
def f(x, y):
    if x > y:
        return 0
    if x == y:
        return 1
    return f(x + 2, y) + f(int(str(x) + '2'), y)


print(f(2, 900))
