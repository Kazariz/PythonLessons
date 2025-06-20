# & - находит общие символы у двух set


# s1 = 'Hello'
# s2 = 'How are you?'
# s3 = set(s1) & set(s2)
# print(s3)
#
# for i in s3:
#     print(i, end=' ')

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a >= b)  # b является подмножеством a
# print(a <= b)
#
# a = {3, 5, 2, 6, 1}
# print(a, type(a))
# lst = list(a)
# print(lst, type(lst))
#
# a = frozenset('hello')
# print(a)
#
# b = frozenset({'hello', 'world'})
# print(b)
#
# c = frozenset({i ** 2 for i in range(10)})
# print(c)

# ===================================================
# Словарь(dict)
# ===================================================
#
# lst = [1, 2, 3]
# d = {"one": 1, 'two': 2, 'three': 3}
# print(lst, type(lst))
# print(d, type(d))
# print(lst[1])  # по индексу
# print(d['two'])  # по ключу
# d['two'] = 200
# print(d, type(d))
#
# d = dict(one=1, two=2)
# print(d, type(d))
#
#
#
# def func(one, two):
#     return one, two
#
#
# print(func(1, 2))
# print(func(two=1, one=2))
#
# lst = [['one', 1], ['two', 2], ['three', 3]]
#
# print(lst)
# print(dict(lst))
#
# d = {0: 'text', 'one': 1, (1, 2): 'кортеж', 'список': [1, 2, 3]}
# print(d)

# from random import randint
#
# d = {randint(1,10): randint(50, 100) for i in range(7)}
# print(d)

# d = {0: 'text', 'one': 1, (1, 2): 'кортеж', 'список': [1, 2, 3]}
# print(d)
# print(d['список'][1])
# print(d[(1, 2)])
# print(d[0])  # не индекс, а ключ
#
# d = {'one': 1, 'two': 2, 'three': 3}
# key = "two5"
# try:
#     print(d[key])
# except KeyError:
#     print('Элемента с ключом', key, 'нет в словаре')
#
# print('one' in d)
# print(2 in d)
# del d['two']
# print(d)  # ключа без значения существовать не может
#
# a = [1, 2, 3]
# print(a)
# del a[1]
# print(a)
#
# for i in d:
#     print(i, d[i])
# Задача ==================================

# spi = {i: input('->') for i in range(1, 5)}
# print(spi)
# delete_el = int(input('Какой элемент удалить: '))
# try:
#     del spi[delete_el]
#     print(spi)
# except KeyError:
#     print('Элемента', delete_el, 'не существует')


# Задача 2 ====================================
# spi = {
#     '1': ['Core i3-4330', 9, 4500],
#     '2': ['Core i5-4670K', 3, 8500],
#     '3': ['AMD FX-6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core i5-3450', 5, 6400]
# }
#
# for i in spi:
#     print(f'{i}) {spi[i][0]} - {spi[i][1]} шт. по {spi[i][2]} руб.')
#
# while True:
#     num = int(input('№: '))
#
#     if num != 0:
#         how_much = int(input('Количество: '))
#         spi[f'{num}'][1] = how_much
#     else:
#         for i in spi:
#             print(f'{i}) {spi[i][0]} - {spi[i][1]} шт. по {spi[i][2]} руб.')
#         break

# ==========================================

# print(dir(dict))
# d = {'one': 1, 'two': 2, 'three': 3}
#
# print(d.keys())
# print(d.values())
# print(d.items())
#
# print(list(d.keys()))
# print(list(d.values()))
# print(list(d.items()))
#
# for i in d:
#     print(i, end=' ')
# print()
# for i in d.values():
#     print(i, end=' ')
#
# for i in d.items():
#     print(i, end=' ')
# print()
#
# for i, j in d.items():
#     print(i, ':', j)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = d.copy()
# print('D =', d)
# print('D2 =', d2)
# d2['four'] = 4
#
# print('D =', d)
# print('D2 =', d2)

# d = {'one': 1, 'two': 2, 'three': 3}
# value = d.get('three', 'Такого элемента не существует')  # получаем значение ключа в переменную
# print(value)
# d = {'one': 1, 'two': 2, 'three': 3}
# value = d.pop('two', 'Такого ключа нет')  # удаляет элемент
# print(value)
# print(d)
#
# d = {'one': 1, 'two': 2, 'three': 3}
# d2 = {'four': 4, 'five': 5, 'six': 6}
# d3 = d | d2  # только со словарем если можем сравнивать
# print(d3)
# d.update(d2)  # обновляет список, может добавлять список кортежей
# print(d)

# Задача 3 =======================================================

# user = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# user2 = {'name': 'Kelly', 'salary': 8000}
# print(user)
# print(user2)
# user.clear()
# print(user)
# user.update(user2)
# print(user)

# Бонус

# print('Анкета')
#
# name = input('Введите свое имя: ')
# age = int(input('Введите свой возраст: '))
# hobby = input('Чем вы увлекаетесь: ')
# love = input('Если ли у вас девушка, если да, то как ее зовут: ')
#
# ank = dict(name=name, age=age, hobby=hobby, love=love)
#
# ank_is_done = f'\n Имя: {name} \n Возраст: {age} \n Хобби: {hobby} \n Отношения: {love}'
# print(ank_is_done)
