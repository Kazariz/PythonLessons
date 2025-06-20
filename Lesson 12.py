# x = 10
# y = 5
# print(f'{x=}, {y=}')
# print(f'{x} x {y} / 2 = {x * y / 2}')
# print(f'{round(45.24234324234, 2)}')
# print(f'{45.24234324234:.5f}')  # сколько символов будет после точки
# num = 74
# print(f'{{{num}}}')  # чтобы выводились скобки с переменной

# dir_name = 'folder'
# file_name = 'file.py'
# print(fr'home\{dir_name}\{file_name}')  # сочетание 2-х атрибутов для экранирования
#
# s = """Многострочный
# текст"""  # более новый тип переноса
# print(s)

# def square(n):
#     """"Принимает число n, возвращает квадрат числа n"""  # красивый комментарий
#     res = n ** 2
#     return res
#
#
# print(square(5))
# print(square.__doc__)  # мой комментарий к функции
# print(len.__doc__)  # комментарий к атрибуту len
# print(min([1, 2, 3, 4, 5]))
# print(max([1, 2, 3, 4, 5]))
# print(len([1, 2, 3, 4, 5]))

# from math import pi
#
#
# def cylinder(r, h):
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#     :param r: положительное число, радиус цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))

# print(ord('a'))  # выводит код символа
# print(ord('#'))
# print(ord('Ц'))

# while True:
#     n = input('-> ')
#     if n == '-1':
#         break
#     else:
#         print(ord(n))

# str = 'Test string for me '
# arr = [ord(x) for x in str]  # создаем список из ASCI кодов каждого символа переменной
# arr = [int(sum(arr) / len(arr))] + arr  # добавляем в начало списка ср. арифметическое
# print('ASCI коды:', arr)
#
# arr += [ord(x) for x in input('-> ')[:3] if
# ord(x) not in arr]  # добавляем в список ASCI коды только первых 3-х введенных символов, если таких кодов нет в списке
# print(arr)
# print(arr.count(arr[-1]) - 1)  # смотрим сколько раз повторяется последний элемент не включая его
# arr.sort(reverse=True)  # сортируем список от большего к меньшему
# print(arr)

# print(chr(97))  # получает символ по его ASCI коду
#
# a = 122
# b = 97
# spi = []
# while a >= 97:
#     spi.append(chr(a))
#     a -= 1
#
# spi.sort(reverse=False)
# for i in spi:
#     print(f'{i} ', end='')

# from random import randint
#
# shortest = 6
# longest = 16
# min_ascii = 33
# max_ascii = 126
#
#
# def random_password():
#     res = ''
#     for i in range(randint(shortest, longest)):
#         res += chr(randint(min_ascii, max_ascii))
#     return res
#
#
# print('Ваш случайный пароль:', random_password())
#
# print(dir(list))
# print(dir(str))

# s = 'hello, WORLD! I am learning Python.'
# print(s.capitalize())  # убирает верхние резисторы в маленькие кроме первой буквы
# print(s.lower())  # hello, world! i am learning python. ОБЯЗАТЕЛЬНО
# print(s.upper())  # HELLO, WORLD! I AM LEARNING PYTHON. ОБЯЗАТЕЛЬНО
# print(s.swapcase())  # HELLO, world! i AM LEARNING pYTHON.
# print(s.title())  # Hello, World! I Am Learning Python.
#
# print(s.lower().count('l'))

# print(s.find('Python'))  # возвращает индекс искомой подстроки, если совпадения нет то возвращает строго -1
# print(s.find('l'))
# print()

# st = 'два один'
# first = st[:st.find(' ')]
# second = st[st.find(' ') + 1:]
# print(second + ' ' + first)

# print(s.rfind('l'))  # последнее вхождение

# print(s.endswith('on.'))  # проверят на что заканчивается переменная
# print(s.endswith('LD!', 10, 13))

# print(s.startswith("I am", 14, ))

# print('abc123'.isalnum())  # есть ли в строке ЦИФРЫ и БУКВЫ
#
# print('ABCabc'.isalpha())  # состоит ли строка только из БУКВ
#
# print('123'.isdigit())  # есть ли в строке только ЦИФРЫ
#
# print('abc'.islower())  # True если все буквы в нижнем регистре, если есть цифры, то тоже True
#
# print('ABC'.isupper())  # True если все буквы в верхнем регистре, если есть цифры, то тоже True

# print('py'.center(50, '-'))  # выравнивается по пробелам и можно отметить пробелы

# print('    py'.lstrip())  # удаляет пробелы СЛЕВА
# print('py    '.rstrip())  # удаляет пробелы СПРАВА
# print('    py     '.strip())  # удаляет пробелы с ОБЕИХ сторон

# print('https://www.python.org'.lstrip('/:htps').strip('.org'))  # также удаляет написанные пользователем символы

# s = 'hello Python! I am learning Python. Мне нравится Python'
# print(s.replace('Python', 'JavaScript', 2))  # меняет слово на другое слово в тексте

# s = '-'
# seq = ('a', 'b', 'c')
# print(s.join(seq))  # вставляет вместо пробелов указанный символ
#
# print('...'.join(['1', '99']))
# print('.'.join('hello'))

# DZ ===================

s = 'Замените в этой строке все появления буквы "о" на букву "О", кроме первого и последняя вхождения.'
first = s[:s.find('о') + 1]
second = s[s.rfind('о'):]
middle = s[s.find('о') + 1:s.rfind('о'):].replace('о', 'О')
print(first + middle + second)
