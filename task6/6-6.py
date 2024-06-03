'''Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует 6 команд: Поднять хвост, означающая переход к перемещению без рисования; Опустить хвост, означающая переход в режим рисования; Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова; Назад n (где n – целое число), вызывающая передвижение в противоположном голове направлении; Направо m (где m – целое число), вызывающая изменение направления движения на m градусов по часовой стрелке, Налево m (где m – целое число), вызывающая изменение направления движения на m градусов против часовой стрелки.
Запись
Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:
Вперёд 2
Повтори 5 [
    Вперёд x Направо 90 Вперёд 3 Направо 90
    Вперёд x Налево 90 Вперёд 1 Налево 90
    ]
Назад 2
Определите, при каком наибольшем натуральном x количество точек с целочисленными координатами внутри области, ограниченной линией, нарисованной Черепахой, и осью абсцисс, меньше 25000. Точки, расположенные на линии, не учитывать.
'''
from turtle import *
screensize(7000, 7000)
tracer(0)
left(90)
k = 20
x = 5
forward(2 * k)
for _ in range(5):
    forward(x * k)
    right(90)
    forward(3 * k)
    right(90)
    forward(x * k)
    left(90)
    forward(k)
    left(90)
backward(2 * k)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5)
done()