spisok = []
length = int(input('Введите длину списка: '))

i = 0
while i < length:
    element = int(input('Введите элемент списка: '))
    spisok.append(element)
    i += 1

print('Список:', spisok)

j = 0
while j < spisok.__len__():
    if spisok[j] < 0:
        spisok.pop(j)
    j += 1

print('Новый список, состоящий из положительных элементов:', spisok)
print('Наибольший элемент списка:', max(spisok))
