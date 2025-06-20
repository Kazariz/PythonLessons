John = {'N': 3056, 'S': 8463, 'E': 8441, 'W': 2694}
Tom = {'N': 4832, 'S': 6786, 'E': 4737, 'W': 3612}
Anne = {'N': 5239, 'S': 4802, 'E': 5820, 'W': 1859}
Fiona = {'N': 3904, 'S': 3645, 'E': 8821, 'W': 2451}


def printlist(lst):
    for i in lst:
        print(i, ':', lst[i])


print('John')
printlist(John)
print('Tom')
printlist(Tom)
print('Anne')
printlist(Anne)
print('Fiona')
printlist(Fiona)

name = input('Имя: ')
region = input('Region: ')
if name == 'John':
    print(John[region])
elif name == 'Tom':
    print(Tom[region])
elif name == 'Anne':
    print(Anne[region])
elif name == 'Fiona':
    print(Fiona[region])
else:
    print('Такого имени или региона не существует')

try:
    new_region = int(input('Новое значение:'))
except ValueError:
    print('Нужно ввести целое число')

if name == 'John':
    John[region] = new_region
    print(John)
elif name == 'Tom':
    Tom[region] = new_region
    print(Tom)
elif name == 'Anne':
    Anne[region] = new_region
    print(Anne)
elif name == 'Fiona':
    Fiona[region] = new_region
    print(Fiona)
else:
    ...

