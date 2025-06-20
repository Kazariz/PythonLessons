# Типы данных
# int - целые числа
# float - дробные числа, 20.5
# str - строковое значение
# bool - true false

# name = 'admin'
# age = 21.5
#
# print(name + str(age))
#
# print(name, type(name))
# print(age, type(age))
#
# a = 4
# b = 5
# print('a =', a, id(a))
# print('b =', b, id(b))
#
# a = b
# print('a =', a, id(a))
# print('b =', b, id(b))

# a = b = c = 5
# a, b, c = 123, 'Hello', 3.14
# print(a)
# print(b)
# print(c)

# print(' ')
# print(' (  )')
# print('  || ')
# print('  || ')
# print('  || ')
# print('  || ')
# print('( )( )')

# import keyword
#
# print(keyword.kwlist)import keyword
#
# print(keyword.kwlist)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)
#
# a = 15
# b = 2
# print('a:', a)
# print('b:', b)
#
# c = a
# a = b
# b = c
#
# print('a:', a)
# print('b:', b)
#
# print('строка символов')
# print("строка символов")
#
# print('Документ \'file.py\' находится по пути: D:\\folder\\file.py')
#
# s1 = 'Hello'
# s2 = 'Python'
# s3 = s1 +' '+s2+' '
# print(s3*5)
#
# a, b, c = 5, 7, 3
# res=a+b+c
# print('Сумма:', res)
# print('Произведение:',a*b*c)
# print('Ср.арифметическое:', res/3)
#
# number = 6+4*5**2+7
# print(number)
#
# num = 2304
# print('Число:',num)
# a = num % 10
# print(a)
# num = num // 10
# b = num % 10
# num = num // 10
# c = num % 10
# num = num // 10
# d = num % 10
#
# print((a*1000)+(b*100)+(c*10)+d)

# print(int(2.987))
# print(round(2.673, 2))


# ===================================================================================================================
# =================LESSON 2==========================================
# ====================================================================================================================
# Flase => '', 0, None


# name = 'Виктор'
# age = 28
# print('Меня зовут', name + '. Мне', age, 'лет.')
# print('Меня зовут', name, '. Мне', age, 'лет.', sep='', end='\n\n')
# print('Вот так')


# name = input('Введите свое имя: ')
# print('Hello', name)
#
# number = int(input('Введите число: '))
# power = int(input('Введите степень: '))
# res = number ** power
#
# print('Число', number, 'в степень', power, '=', res)

# b1 = True - только в ВЕРХНЕМ РЕГИСТРЕ
# b2 = False
# print(b1, type(b1))

# b1 = True - 1
# b2 = False - 0
#
# print(b1 + 5)
# print(b2 + 5)

# print('hello'>'HELLO')

# cnt = 5
#
# if cnt < 10:
#     cnt = cnt + 1
# print(cnt)
#
# age = int(input('Введите свой возраст: '))
#
# if age >= 18:
#     print('Доступ на сайт разрешен')
#     print('Добро пожаловать!')
#     # pass
# else:
#     print('Доступ запрещен!')
#     # ...
#
# import this
# print(this)

# a = 15
# b = 25
#
# if a > b:
#     print('a > b')
# else:
#     print('b > a')

# a = int(input('Введите первую сторону: '))
# b = int(input('Введите вторую сторону: '))
# c = int(input('Введите третью сторону: '))
#
# if a == b == c:
#     print('Треугольник равносторонний')
# elif a == b or b == c or a == c:
#     print('Треугольник равнобедренный')
# else:
#     print('Треугольник разносторонний')

# day = int(input('Введите день недели (цифрой): '))
# if 1 <= day <= 5:  # (day >= 1) and day <= 5
#     print('Рабочий день - ', end='')
#     if day == 1:
#         print('понедельник')
#     elif day == 2:
#         print('вторник')
#     elif day == 3:
#         print('среда')
#     elif day == 4:
#         print('четверг')
#     else:
#         print('пятницы')
# elif day == 6 or day == 7:
#     print('Выходной день - ', end='')
#     if day == 6:
#         print('суббота')
#     else:
#         print('воскресенье')
# else:
#     print('Такого дня недели не существует')

# time = int(input('Введите номер месяца: '))
# if 1 <= time <= 2:
#     print('Зима')
# elif time == 12:
#     print('Зима')
# elif 3 <= time <= 5:
#     print('Весна')
# elif 6 <= time <= 8:
#     print('Лето')
# elif 9 <= time <= 11:
#     print('Осень')
# else:
#     print('Такого месяца не существует')

# crows = int(input('Введите количество ворон (от 0 до 9): '))
# if 0 <= crows <= 9:
#     print('На ветке', crows, end=' ')
#     if crows == 1:
#         print('ворона')
#     elif 2 <= crows <= 4:
#         print('вороны')
#     else:
#         print('ворон')
# else:
#     print('Ошибка ввода данных')


# ====================================================================================================================
# =================LESSON 3==========================================
# ====================================================================================================================

# Тернарное выражение

# a, b = 20, 30
# print('a==b' if a == b else 'a > b' if a > b else 'a < b')
# try:
#     n = int(input('Введите целое цифру: '))
#     print(2 / n)
# except (ValueError, ZeroDivisionError):
#     print('Что то пошло не так')
# else:
#     print('Все нормально ты ввел, не парься мужик')
# finally:
#     print('Конец программы')

# first = input('Введите первое число: ')
# second = input('Введите второе число: ')
# try:
#     print(int(first) + int(second))
# except ValueError:
#     print(first + second)

# Циклы

# i = 0
# while i < 5:
#     print('i =', i)
#     i += 1  # изменение счетчика

# Итерация - один шаг цикла

# i = 10
# while i > 0:
#     print('i =', i)
#     i -= 0.1

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print('i =', i)
#     i += 1

# n = int(input('Введите кол-во звезд: '))
# print('*' * n)

# a = int(input('Введите начало диапазона: '))
# b = int(input('Введите конец диапазона: '))
#
# while a <= b:
#     if a % 2:
#         print('a =', a)
#     a += 1

# n = input('Введите целое число:')
#
# while type(n) is not int:
#     try:
#         n = int(n)
#     except ValueError:
#         print('Число не целое')
#         n = input('Введите целое число:')
#
# if n % 2 == 0:
#     print('Число четное')
# else:
#     print('Число нечетное')

# res = 1
# while True:
#     n = int(input('Введите число: '))
#     if n == 0:
#         break
#     else:
#         res *= n
# print('Произведение:', res)

# i = 0
# while i < 10:
#     print(i)
#     i += 1
# else:
#     print('Цикл окончен, i =', i)

# i = 1
# while i < 5:
#     print('Внешний цикл i =', i)
#     j = 1
#     while j < 4:
#         print('\tВнутренний цикл j =', j)
#         j += 1

# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, '*', j, '=', i * j, end='\t\t')
#         j += 1
#     print()
#     i += 1

# i = 0
# while i < 7:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print('+', end='')
#         else:
#             print('-', end='')
#         j += 1
#     print()
#     i += 1
#
# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(' ', end='')
#         j += 1
#     print('*')
#     i += 1

# from math import pi
#
# radius = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * pi * radius, 2))

import time
import locale

# print(time.time())

# print(time.ctime())

# print(time.localtime())
# print()
# res = time.localtime()
# print(res.tm_year)
# print(time.strftime('%m/%d'))
#
# locale.setlocale(locale.LC_ALL, locale='ru')
# print(time.strftime('%B %d, %Y'))


# def hello(name):
#     print('Hello', name)
#
#
# hello('Ivan')

# def get_sum(a, b):
#     return a + b
#
#
# res = get_sum(5, 8)
# print(res)

# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['С', 'л', 'о', 'н']))\

# ==================================================================== LESSOn 4 =============================

# t1 = tuple('Hello')
# t2 = tuple('world')
# t3 = t1 + t2
# print(t3.count('l'))
#
#


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return tuple()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

# from random import randint
#
#
# def ran(start, end):
#     return tuple(randint(start, end) for i in range(10))
#
#
# tpl1 = ran(0, 5)
# print(tpl1)
# tpl2 = ran(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3)
# print('0 =', tpl3.count(0))

# point = (0, 10)
#
# match point:
#     case (0, 0):
#         print('Точка находится в координате 0:0')
#     case (x, 0):
#         print('Точка находится в', x, 'по оси x и в 0 координате по оси Y')
#     case (0, y):
#         print('Точка находится в 0 по оси x и в', y, 'координате по оси Y')
#     case _:
#         print('Это координаты точки')
#
# t = (10, 'Python', (1, 2, 3), [4, 5, 6], ['hello', 'world'])
# print(t)
# t[4][0] = 'new'
# print(t)

# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# first_name, year, married = get_user()
# print(first_name, year, married)

# ===================================================   LESSON 5 ====================================================

# s1 = 'Hello'
# s2 = 'How are you'
# s3 = set(s1) & set(s2)
# print('Общими буквам являются:')
# for i in s3:
#     print(i, end=' ')
#
# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
#
# print(a >= b)

# a = {14, 54, 2, 3, 54}
# print(a, type(a))
#
# lst = list(a)
# print(lst, type(lst))
#
# b = set(lst)
# print(b, type(b))

# ====================================================== LESSON 6 ===================================================

# def add(a):
#     x = 2
#
#     def inner():
#         print('x=', x)
#         return a + x
#
#     return inner()
#
#
# print(add(3))
# =============================== LESSON 7 ================================

import re

s = 'Я ищу совпадения в 2025 году. И я их найду в 2 счета'
reg = 'я'

# print((re.findall(reg, s)))
# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())

# print(re.split(reg, s))  # удаляет элемент из списка


