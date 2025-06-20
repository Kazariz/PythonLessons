moneys = int(input('Введите кол-во копеек от 1 до 99: '))
if 1 <= moneys <= 99:
    print(moneys, end=' ')
    ostatok = moneys % 10
    if ostatok == 1 or moneys == 1:
        print('копейка')
    elif moneys == 14:
        print('копеек')
    elif 2 <= ostatok <= 4 or moneys == 3 or moneys == 4 and moneys != 14:
        print('копейки')
    else:
        print('копеек')
else:
    print('Ошибка')


