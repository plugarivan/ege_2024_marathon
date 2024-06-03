'''Исполнитель Цапля действует на плоскости с декартовой системой координат. В начальный момент Цапля находится в начале координат, её клюв направлен вдоль положительного направления оси ординат, клюв опущен. При опущенном клюве Цапля оставляет на поле след в виде линии. В каждый конкретный момент известно положение исполнителя и направление его движения. У исполнителя существует три команды: Вперёд n (где n  — целое число), вызывающая передвижение Цапли на n единиц в том направлении, куда указывает её клюв; Направо m (где m  — целое число), вызывающая изменение направления движения на m градусов по часовой стрелке; Дуга r, a, b, α (где r, a, b, α  — целые числа), вызывающая передвижение Цапли из текущей точки с координатами (x, y) по дуге окружности с центром в точке с координатами (x + a, y + b) и радиусом r, градусная мера дуги равна α, движение по дуге идёт по часовой стрелке.
Запись Повтори k [Команда1 Команда2 ... КомандаS] означает, что последовательность из S команд повторится kраз.
Цапле был дан для исполнения следующий алгоритм:
Направо180 Вперёд5 Направо90 Вперёд50 Направо90 Вперёд5 Повтори5 [Дуга 5, 5, 0, 180].
Определите, сколько точек с целочисленными координатами будут находиться внутри области, ограниченной линией, заданной данным алгоритмом. Точки на линии учитывать не следует.
'''
from turtle import *
tracer(0)
k = 10
left(90)
right(180)
forward(5 * k)
right(90)
forward(50 * k)
right(90)
forward(5 * k)
for i in range(5):
    seth(90)
    circle(-5 * k, 180)
pu()
for x in range(-k, k):
    for y in range(-k, k):
        goto(x * k, y * k)
        dot(5)
done()