# a = ()
# print(a, type(a))
#
# b = tuple('Hello')
# print(b, type(b))
from operator import index

# a = 1, 2, 3, 4, 5
# print(a, type(a))
# print(a[2])
# print(a[1:4])

# s = tuple(int(input('-> ')) for i in range(5))
# print(s)

# from random import randint
#
# s = tuple(randint(50, 100) for i in range(5))
# print(s)

# t1 = tuple('hello')
# t2 = tuple('world')
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3)
# print(t3*3)
# print(t3.count('o'))
# if 'l' in t3:
#     print(t3.index('l'))
# else:
#     print('Такого символа нет')
# print(t3.index('l', 4))
# for i in t3:
#     print(i, end=' ')


# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#             first = tpl.index(el)
#             second = tpl.index(el, first + 1)
#             return tpl[first:second + 1]
#         else:
#             return tpl[tpl.index(el):]
#     else:
#         return ()
#
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))
# from random import randint
#
#
# def full(a, b):
#     return tuple(randint(a, b) for i in range(10))
#
#
# tpl1 = full(0, 5)
# print(tpl1)
# tpl2 = full(-5, 0)
# print(tpl2)
# tpl3 = tpl1 + tpl2
# print(tpl3, '\n0 =', tpl3.count(0))


# point = (1, 5)
#
# match point:
#     case (0, 0):
#         print('Точка находится в координате 0:0')
#     case (x, y):
#         print('Точка находится в координате', x, ':', y)
#     case (x, 0):
#         print('Точка находится в координате', x, ': 0')
#     case (0, y):
#         print('Точка находится в координате 0 :', y)
#     case _:
#         print('Это не координата')


# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'], 'python')
# print(t)
# t[4][0] = 'new'
# print(t)
# t[4].append('hi')
# print(t)

# Распаковка кортежа

# t = (1, 2, 3)
#
# x = t[0]
# y = t[1]
# z = t[2]
# print(x, y, z)

#
# def get_user():
#     name = 'Tom'
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# user = get_user()
# print(user)
# first_name, aged, married = get_user()
# print(first_name, aged, married)

# t = (1, 2, 3)
# del t  # можно удалить, но не удалять

# t = (1, 2, 3, 4, 5)
# print(t, type(t))
# lst = list(t)
# print(lst, type(lst))
# lst.append(6)
# tpl = tuple(lst)
# print(tpl, type(tpl))  # гениальная фича для добавления элементов в кортеж

# countries = (
#     ('Russia', 190.5, (('Moscow', 55.3), ('Dzerzhinsk', 14.2))),
#     ('USA', 150.3, (('New York', 24.4), ('Nigers', 50.2)))
# )
#
# for i in countries:
#     country_name, country_population, cities = i
#     print('\nСтрана:', country_name, 'население:', country_population)
#     for city in cities:
#         city_name, city_population = city
#         print('\tГород:', city_name, 'население =', city_population)

#
# a = input('Введите по порядку, без пробелов, элементы кортежа: ')
# b = tuple(a)
# lst = []
#
# for i in range(len(a)):
#     if b[i] not in lst:
#         lst.append(b[i])
#
# for i in range(len(lst)):
#     print('Количество', lst[i], '=', b.count(lst[i]))

# Множество (set)
#
# s = {'one', 'two', 'three'}
# print(s, type(s))

# lst = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# print([i for i in lst if 'a' in i])
# print(tuple(i for i in lst if 'a' in i))

# s = {1, 2, 3, 4, 5}
# print(s)
# s.add(6)
# print(s)
# s.remove(2)  # - удаляет элемент по значению
# s.discard(2)  # - удаляет или может не удалять если нету такого элемента
# print(s)

a = {43245, 34534}
s = {1, 2, 3, 4}
# print(s)
# s.pop()  # - удаляет первый элемент
# print(s)
# s.clear()
# print(s)  # - очищает сет
print(a.union(s))  # - объединяет сеты
