import math

print('Какой фигуры найти площадь?\n 1 - прямоугольник 2 - треугольник 3 - круг ')
try:
    change = int(input('Введите номер варианта:'))

except (ValueError, NameError):
    print('Такого варианта нет :)')


def pryamoug():
    try:
        side = int(input('Введите длину: '))
        side2 = int(input('Введите ширину: '))
        print('Площадь прямоугольника:', float(side * side2))
    except ValueError:
        print('Такого варианта нет')


def treug():
    try:
        side = int(input('Введите основание: '))
        side2 = int(input('Введите высоту: '))
        print('Площадь прямоугольника:', float(side * side2 / 2, 2))
    except ValueError:
        print('Такого варианта нет')


def ball():
    try:
        side = int(input('Введите радиус: '))
        print('Площадь прямоугольника:', round(math.pi * side ** 2, 2))
    except ValueError:
        print('Такого варианта нет')


try:
    if change == 1:
        pryamoug()
    elif change == 2:
        treug()
    elif change == 3:
        ball()
    else:
        print('Такого варианта нет')
except NameError:
    ...
