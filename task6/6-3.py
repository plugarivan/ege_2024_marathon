'''Исполнитель Черепаха действует на плоскости с декартовой системой координат. В начальный момент Черепаха находится в начале координат, её голова направлена вдоль положительного направления оси ординат, хвост опущен. При опущенном хвосте Черепаха оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. . У исполнителя существует 6 команд: Поднять хвост, означающая переход к перемещению без рисования; Опустить хвост, означающая переход в режим рисования; Вперёд n (где n – целое число), вызывающая передвижение Черепахи на n единиц в том направлении, куда указывает её голова; Назад n (где n – целое число), вызывающая передвижение в противоположном голове направлении; Направо m (где m – целое число), вызывающая изменение направления движения на m градусов по часовой стрелке, Налево m (где m – целое число), вызывающая изменение направления движения на m градусов против часовой стрелки.
Запись

Повтори k [Команда1 Команда2 … КомандаS]
означает, что последовательность из S команд повторится k раз. Черепахе был дан для исполнения следующий алгоритм:

Повтори 2 [Вперёд 10 Направо 90 Вперёд 20 Направо 90]
Поднять хвост
Вперёд 5 Направо 90 Вперёд 7 Налево 90
Опустить хвост
Повтори 2 [Вперёд 20 Направо 90 Вперёд 40 Направо 90]
Определите, сколько точек с целочисленными координатами будут находиться внутри пересечения фигур, ограниченных заданными алгоритмом линиями, включая точки на границах этого пересечения.
'''
from turtle import *

tracer(0)
left(90)
k = 20
for _ in range(2):
    forward(10 * k)
    right(90)
    forward(20 * k)
    right(90)
pu()
forward(5 * k)
right(90)
forward(7 * k)
left(90)
pd()
for _ in range(2):
    forward(20 * k)
    right(90)
    forward(40 * k)
    right(90)
pu()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5)
done()
