# import math
# from math import sqrt, ceil, floor
# import math as m
# from math import *
#
# num1 = sqrt(2)  # корень
# num2 = ceil(3.2)  # округление
# num3 = floor(3.8)  # округление вниз
# print(num1)
# print(num2)
# print(num3)

# from math import *
#
# radius = int(input('Введите радиус окружности: '))
# print('Длина окружности:', round(2 * pi * radius, 2))

# Data and Time

import time
import locale

# print(time())
# print(ctime())
# print(localtime())
res = time.localtime()


# print(res.tm_year)

# print(strftime('%m/%d/%Y, %H:%M:%S'))

# print(time.strftime('Today is %m/%d/%Y, %H:%M:%S'))
# locale.setlocale(locale.LC_ALL, 'ru')
# print(time.strftime('Сегодня: %B %d, %Y'))
#
# num = 1000000
# print(num)

# pause = 2
# print('Start')
# time.sleep(pause)
# print(pause, 'second')
#
# start = time.time()
# time.sleep(5)
# finish = time.time() - start
# print(finish)


# FUNCTION
#
# def hello(name, age):
#     print('Привет, меня зовут', name, 'мне', age, 'лет.')
#
#
# hello('Иван', 16)


# def get_sum(a, b):
#     return a + b
#
#
# summa = get_sum(1, 7)
# print(summa)


# def change(lst):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst

# def change(lst):
#     end = lst.pop()
#     start = lst.pop(0)
#     lst.append(start)
#     lst.insert(0, end)
#     return lst
#
#
# print(change([1, 2, 3]))
# print(change([9, 12, 33, 54, 105]))
# print(change(['с', 'л', 'о', 'н']))

def test(x, y):
    if x > y:
        return True
    else:
        return False


# print(test(8, 5))
# print(test(5, 8))

# num1 = 10
# num2 = 5
#
# if test(num1, num2):
#     print(num1, '>', num2)
#
# else:
#     print(num1, '<', num2)

# def check_password(password):
#     has_upper = False
#     has_lower = False
#     has_number = False
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         if "a" <= ch <= "z":
#             has_lower = True
#         if "0" <= ch <= "9":
#             has_number = True
#
#     if len(password) >= 8 and has_upper and has_lower and has_number:
#         return True
#     return False
#
#
# p = input('Введите пароль:')
# if check_password(p):
#     print('Это надёжный пароль')
# else:
#     print('Это ненадёжный пароль, советуем вам его поменять.')


# def get_sum(a, b, c=1, d=0):
#     return a + b + c + d
#
#
# print(get_sum(1, 5, d=6))

# def display_info(name, age):
#     print('Name:', name, '\nAge:', age)
#
#
# display_info(age=23, name='Иван')


# a = 'Hello'
# b = 'Hello'
# # print(a == b)
# # print(a is b)
#
#
# lt1 = [1, 2, 3]
# print(lt1, id(lt1))
# lt1.append(4)
# print(lt1, id(lt1))

lst = [10, 20, 30]
tpl = (10, 20, 30)
print(lst.__sizeof__())
print(tpl.__sizeof__())

# print(lst[1])
# print(tpl[1])
