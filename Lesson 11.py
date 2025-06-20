# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# print(list(map(lambda x, y: x + y, l1, l2)))
#
# t = ('abcd', 'abc', 'adrfg', 'def', 'huy')
#
# t2 = list(filter(lambda s: len(s) == 3, t))  # фильтруем список по назначенной длине, фильтрует данные
# print(t2)
#
# b = [66, 77, 88, 99, 234, 65, 123, 65, 98, 45]
# res = list(filter(lambda s: s > sum(b) / len(b), b))
# print(res)
#
# print(list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(1, 10)))))
# print(list(filter(lambda x: x % 2, range(1, 10))))
from itertools import count


# print([x ** 2 for x in range(1, 10) if x % 2])  # квадраты не четных чисел


# Декораторы (связано с замыканием)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# def super_func(func):
#     print('Hello, I am "surer func"')
#     print(func())
#
#
# super_func(hello)

# def hello():
#     return 'Hello, I am func "hello"'
#
#
# test = hello  # присваивание пишется БЕЗ СКОБОК
# print(test())

# def my_decorator(func):  # декорирующая функция
#     def inner():
#         print('Код до вызова функции')
#         func()
#         print('Код после вызова функции')
#
#     return inner
#
#
# @my_decorator  # Декоратор. присваивает к другой функции, то есть == my_decorator(func_test) и работает как замыкание
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()

# def bold(fn):
#     def wrap():
#         return '<b>' + fn() + '</b>'
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return '<i>' + fn() + '</i>'
#
#     return wrap
#
#
# @bold
# @italic
# def hello():
#     return 'text'
#
#
# print(hello())

# def cnt(fn):
#     count = 1
#
#     def wrap():
#         nonlocal count
#         fn()
#         print('Вызов функции:', count)
#         count += 1
#
#     return wrap
#
#
# @cnt
# def hello():
#     print('Hello')
#
#
# @cnt
# def world():
#     print('World')
#
#
# hello()
# hello()
# hello()
# world()
# world()
# hello()

# def outer(fn):
#     def wrap(arg1, arg2):
#         print('Данные:', arg1, arg2)
#         fn(arg1, arg2)
#
#     return wrap
#
#
# @outer
# def print_full_name(first, last):
#     print('Меня зовут', first, last)
#
#
# print(print_full_name('Ирина', 'Ветрова'))

# def outer(fn):
#     def wrap(*arg1, **kwargs):
#         fn(*arg1, **kwargs)
#
#     return wrap
#
#
# def print_students(a, b, c, study='Python'):
#     print(f'{a}, {b}, {c} изучают {study} \n')
#
#
# print_students('Борис', 'Елизавета', 'Светлана', study='JavaScript')
# print_students('Борис', 'Елизавета', 'Светлана')

# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(args1, x, args2, y, '=', end=' ')
#             fn(x, y)
#
#         return wrap
#
#     return args_dec
#
#
# @decor('Сумма:', '+')
# def summa(a, b):
#     print(a + b)
#
#
# @decor('Разность:', '-')
# def sub(a, b):
#     print(a - b)
#
# summa(5, 2)
# sub(5, 3)

# Задача 1 # сложная задача, надо понимать

# def multiply(arg):
#     def outer(fn):
#         def inner(args):
#             return arg * fn(args)
#
#         return inner
#
#     return outer
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# def typed(*args, **kwargs):  # что приходит из декоратора
#     def wrapper(fn):  # функция которая возвращает данные
#         def wrap(*f_args, **f_kwargs):  # данные возвращающей функции
#             for i in range(len(args)):
#                 if type(f_args[i]) is not args[i]:
#                     raise TypeError('Некорректный тип данных')
#
#             for k in kwargs:
#                 if type(f_kwargs[k]) is not kwargs[k]:
#                     raise TypeError('Некорректный тип данных для именованного параметра')
#
#             return fn(*f_args, **f_kwargs)
#
#         return wrap
#
#     return wrapper
#
#
# @typed(int, int, int)
# def typed_fn(x, y, z):
#     return x * y * z
#
#
# @typed(str, str, str)
# def typed_fn2(x, y, z):
#     return x + y + z
#
#
# @typed(str, str, int)
# def typed_fn3(x, y, z):
#     return (x + y) * z
#
#
# print(typed_fn(3, 4, 5))
# # print(typed_fn(3, 4, 'Hello'))
# print(typed_fn2('hi ', 'im ', 'ivan'))
# print(typed_fn3('Hello ', 'world ', 'sdf '))

# DZ

def decorator(fn):
    def wrapper(*args, **kwargs):
        print(f'Сумма чисел: ', end='')
        for i in args:
            print(f'{i}, ', end='')
        print('=', fn(*args))
        arif = fn(*args) / args.__len__()
        print(f'Среднее арифметическое чисел: ', end='')
        for i in args:
            print(f'{i}, ', end='')
        print('=', arif)
        return arif

    return wrapper


@decorator
def summa(*args):
    return sum(args)


summa(2, 3, 3, 4)
# DONE ============
#
# print(bin(18))  # двоичная система счисления 10010
# print(oct(18))  # восьмеричная система счисления 22
# print(hex(18))  # шестнадцатеричная система счисления 12
#
# print(0b10010)
# print(0o22)
# print(0x12 + 0b10010)
#
# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# print(e * 2)
#
# s = 'Hello'
# print(s, id(s))
#
# s = s + '!'
# print(s, id(s))  # уже другая, новая переменная
# print(s[1])
# print(s[1:3])
# print('H' in s)
# # str - неизменяемый
#
# print('Hello')
# print(u'Hello') # unicode
#
# print('C:\\folder\\file.py')
# print(r"C:\folder\file.py\\"[:-1])
# print(r'C:\folder\file.py')  # убирает экранирование

# print(b'a1b2c3')  # для отображения байтовых файлов

# name = 'Иван'
# age = 16
# print(f'Меня зовут {name}, мне {age} лет.')
# def decorator(func):
#     def wrapper():
#         print('Начало кода')
#         func()
#         print('Конец кода')
#
#     return wrapper
#
#
# @decorator
# def hello():
#     print('Hello world!')
#
#
# hello()
