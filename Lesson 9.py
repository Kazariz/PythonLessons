# user = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
# user['location'] = user.pop('city')  # заменяет ключ на другое название, удаляя прошлый
# print(user)


# s = {
#     'first': {
#         1: 'one',
#         2: 'two',
#         3: 'three'
#     },
#     'second': {
#         4: 'four',
#         5: 'five'
#     }
# }
#
# print(s)
#
# for x in s:
#     print(x)
#     for y in s[x]:
#         print(f'\t {y}: {s[x][y]}')
# print()
#
# for x, y in s.items():
#     print(x)
#     for i, j in y.items():
#         print('\t', i, ': ', j, sep='')

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print({value: key for key, value in d.items()})
#
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# print({key: value for key, value in d.items() if value <= 2})
#
# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
#
# print(list(d.items()))

# Задача 1 =========================================

# spi = ['one', 1, 2, 3, 'two', 10, 20, 'three', 15, 36, 60, 'four', -20]
# spi2 = dict()
# for i in spi:
#     if type(i) is str:  # type(i)==str
#         spi2[i] = []  # создаем ключ когда встречаем тип str
#         s = i  # сохраняем ключ в переменную
#     else:
#         spi2[s].append(i)  # с помощью сохраненной переменной, добавляем в нее элементы с типом int
#
# print(spi2)  # выводим готовый dict

# =zip===============================================

# a = ['Декабрь', 'Январь', 'Февраль', 'Март']
# b = [12, 1, 2, 3]
# c = [1.0, 2.0, 3.0, 4.0]
# print(dict(zip(a, b)))
# print(list(zip(a, b)))
# print(tuple(zip(a, b, c)))
#
# month = [('Декабрь', 12), ('Январь', 1), ('Февраль', 2), ('Март', 3)]
# a, b = zip(*month)  # с помощью звездочки и zip, распаковываем список
# print(a)
# print(b)


# one = {'name': 'Irina', 'surname': 'Petrova', 'job': 'Consultant'}
# two = {'name': 'Igor', 'surname': 'Vetrov', 'job': 'Manager'}
#
# for (k1, v1), (k2, v2) in zip(one.items(), two.items()):
#     print(k1, '->', v1)
#     print(k2, '->', v2)
#
# one = {'name': 'Irina', 'surname': 'Petrova', 'job': 'Consultant'}
# print(sorted(one.items()))

# letters = ['b', 'a', 'c', 'd']
# numbers = [3, 4, 1, 2]
#
# lst = list(zip(letters, numbers))
# print(lst)
# lst.sort()
# print(dict(lst))
#
# lst2 = list(zip(numbers, letters))
# print(lst2)
# lst2.sort()
# print(dict(lst2))
# print({v: k for k, v in lst})
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)

# one = {'one': 1, 'two': 2}
# two = {'three': 3, 'four': 4}
# print({**one, **two})  # {'one': 1, 'two': 2, 'three': 3, 'four': 4}

# a = ['Январь', 'Февраль', 'Март']
# i = 1
# for value in a:
#     print(f'{i}) {value}')
#     i += 1
# print()
# for i, value in enumerate(a, 1):
#     print(f'{i}) {value}')

# one = {'name': 'Irina', 'surname': 'Petrova', 'job': 'Consultant'}
#
# for i, (k, v) in enumerate(one.items(), 1):
#     print(f'{i}) {k} -> {v}')

# def func(*args):
#     return args
#
#
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6))
# print(summa(3, 4, 5))

# def med_arif(*params):
#     summ = 0
#     length = params.__len__()
#     for i in params:
#         summ += i
#     arif = summ / length
#     print(arif)
#     spi = []
#     for i in params:
#         if i < arif:
#             spi.append(i)
#     return spi
#
#
# print(med_arif(1, 2, 3, 4, 5, 6, 7, 8, 9))

# def func(a, *args):
#     return a, args
#
#
# print(func(1, 53454353, 6456, 4654645, 6456, 45, 646))

# def print_scores(student, *scores):
#     print(f'Имя студента: {student}. Баллы: ', end='')
#     for score in scores:
#         print(score, end=', ')
#
#
# print(print_scores('Irina', 100, 95, 80, 92, 99))
# print(print_scores('Igor', 34, 65, 12, 54, 23))

# def func(**kwargs):
#     return kwargs
#
#
# print(func(a=1, b=2, c=3))
# print(func())
# print(func(one=1))

# def info(**data):
#     for k, v in data.items():
#         print(f'{k}: {v} ')
#     print('\n')
#
#
# info(name="Irina", surname='Vertova', age=22, phone='22-33-44')
# info(name="Igor", age=12, phone='99-73-54', email='igor@mail.com')

# def func(a, b, *args, **kwargs):  # нельзя создавать два и больше аргументов с одинаковым количеством звездочек
#     print(args[0])
#     return a, b, args, kwargs
#
#
# print(func(1, 2, 3, 4, 5, 6, c=47, d=54, e=79))

# Области видимости (scope) ================================================

# name = 'Tom'  # Global
#
#
# def hi():
#     global name, surname
#     name = 'Same'  # Local
#     surname = 'Jonson'
#     print('Hello', name, surname)
#
#
# def bye():
#     print('Bye', name)
#
#
# hi()
# bye()
# print(name)
# print(surname)

# import builtins
#
# names = dir(builtins)
# for t in names:
#     print(t)

# max = 5
# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(max[lst])
