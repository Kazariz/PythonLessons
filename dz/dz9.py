students = int(input('Количество студентов: '))
i = 1
spi = {}
all_points = 0
while i <= students:
    print(i, end='')
    print('-й студент: ', end='')
    st_Name = input()
    point = int(input('Балл: '))
    spi[st_Name] = point
    all_points += point
    i += 1

medium_point = all_points / students
print('Средний балл:', round(medium_point), end='')
print('. Студенты с баллом выше среднего:')
for j in spi:
    if spi[j] > medium_point:
        print(j)
