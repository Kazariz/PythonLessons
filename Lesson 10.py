# def add(a):
#     x = 2
#
#     def inner():
#         print(f'x  = {x}')
#         return a + x
#
#     return inner()  # возвращает данные из функции
#
#
# print(add(3))


# def outer():
#     a = 6
#
#     def inner(b):
#         a = 4
#         print(f'Сумма: {a + b}')
#
#     print(a)
#     inner(5)
#
#
# outer()

x = 25
t = 0


# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a  # делаю ее НЕ локальной, тем самым она становится видна функции на уровень выше
#         a = 35
#         print(f'a = {a}')
#
#     inner()
#     t = a
#
#
# fn()
#
# c = x + t
# print(c)
#
# x = 5
#
#
# def f1():
#     x = 25  # 55
#
#     def f2():
#         # x = 33
#
#         def f3():
#             nonlocal x  # работает только если есть такая же переменная в функциях выше
#             x = 55
#
#         f3()
#         print('fn2.x =', x)  # 33
#
#     f2()
#     print('fn1.x =', x)  # 25
#
#
# f1()
# print(x)

#
# def outer(a1, b1, a2, b2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + b2
#
#     inner()
#     return [a, b]
#
#
# print(outer(2, 3, -1, 4))
#
# def func1():
#     a = 1
#     b = 'line'
#     c = [1, 2, 3]
#
#     def func2():
#         nonlocal a  # так надо делать, если тип данных неизменяемый
#         c.append(4)
#         print(a)
#         a = a + 1
#         return a, b, c
#
#     return func2()
#
#
# print(func1())

# Замыкание ============================================
#
# def outer(n):
#     def inner(x):
#         return n + x
#
#     return inner  # возвращаем функцию без скобок для переменной
#
#
# p1 = outer(5)  # переменная == функция
# print(p1(10))
#
# p2 = outer(6)
# print(p2(11))
#
# print(outer(5)(4))


# Задача 1 ====================================================================================
#
# def func(city):
#     a = 0
#
#     def inner():
#         nonlocal a
#         a += 1
#         print(city, a)
#
#     return inner
#
#
# res1 = func('Москва')
# res1()
# res1()
# res1()
# res2 = func('Япония')
# res2()
# res2()
# res1()


# Анонимные функции (Lambda - выражения)

# print((lambda x, y: x + y)(1, 2))

# Задача 2 ================================

# print((lambda x, y: x ** 2 + y ** 2)(2, 5))  # сумма квадратов


# print((lambda a, b, c: a + b + c)(1, 2, 3))
# print((lambda a, b, c=3: a + b + c)(1, 2))
# print((lambda *args: sum(args))(1, 2, 3, 4, 5, 6))

# c = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4
# )
#
# for t in c:
#     print(t('abc___'))

#
# def outer(n):
#     return lambda x: n + x
#
#
# f = outer(5)
# print(f(2))

# def sort_list(i):
#     return i[i]
#
#
# d = {'b': 3, 'c': 1, 'a': 2}
# lst = list(d.items())
# print(lst)
# lst.sort(key=sort_list())
# print(lst)
# print(dict(lst))  # отсортировали dict по данным с помощью списка

# Задача 3 ============================================================

# players = [
#     {'name': 'Антон', 'last_name': 'Бирюков', 'raiting': 9},
#     {'name': 'Алексей', 'last_name': 'Бодня', 'raiting': 10},
#     {'name': 'Федор', 'last_name': 'Сидоров', 'raiting': 4},
#     {'name': 'Михаил', 'last_name': 'Семенов', 'raiting': 6}
# ]
#
# print(sorted(players, key=lambda i: i['last_name']))
# print(sorted(players, key=lambda i: i['raiting'], reverse=True))
# print(sorted(players, key=lambda i: i['raiting']))

#
# lst = [(lambda x, y: x + y), (lambda x, y: x - y), (lambda x, y: x * y), (lambda x, y: x / y)]
# print(lst[0](10, 5))
#
# d = {
#     1: lambda: print('Понедельник'),
#     2: lambda: print('Вторник'),
#     3: lambda: print('Среда'),
#     4: lambda: print('Четверг'),
#     5: lambda: print('Пятница'),
#     6: lambda: print('Суббота'),
#     7: lambda: print('Воскресенье')
# }
#
# d[3]()  # обязательно для вызова круглые скобки

# print((lambda a, b: a if a > b else b)(5, 7))


# map(func, *iterable), filter(func, *iterable)

# def mult(t):
#     return t * 2
#
#
# lst = [2, 8, 12, -5, -10]
# print(list(map(mult, lst)))  # умножили каждый элемент на 2, !! главное указать тип данных !!
#
# print(list(map(lambda t: t * 2, lst)))
# print(list(map(lambda t: t * 2, [2, 8, 12, -5, -10])))
#
# t = (2.88, -1.75, 100.55)
#
# print(list(map(lambda x: int(x), t)))  # округлили все элементы списка
# print(list(map(int, t)))  # упрощенная версия, встроенная функция
#
# st = ['a', 'b', 'c', 'd', 'e', 'f']
# num = [1, 2, 3, 4, 5]
# val = [2.0, 5.4, 7.8, 9.4, 7.4]
# print(tuple(map(lambda x, y, z: (x, y, z), st, num, val)))


# DZ

def plosh(a, b, c):
    ploshad = 0

    def second_plosh():
        nonlocal ploshad
        ploshad = 2 * (a * b + b * c + a * c)
        return ploshad

    return second_plosh()


print(plosh(2, 4, 6))
print(plosh(5, 8, 2))
print(plosh(1, 6, 8))

# ======= DONE ==================
