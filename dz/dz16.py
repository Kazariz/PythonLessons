lines = [
    "Замена строки в текстовом файле;",
    "изменить строку в списке;",
    "записать список в файл;"
]

pos1 = 1
pos2 = 2

lines[pos1], lines[pos2] = lines[pos2], lines[pos1]

for line in lines:
    print(line)
