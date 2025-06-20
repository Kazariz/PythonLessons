# Найти ср.арифметическое

n = int(input('n = '))
i = 0
arifm = 0
schet = 0

while i < n:
    num = int(input('-> '))
    if num > 0:
        arifm += num
    else:
        arifm += 0
        schet += 1

    i += 1

n -= schet
print('Среднее арифметическое:', float(arifm / n))
