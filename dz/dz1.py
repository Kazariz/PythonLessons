num = 97531
print('Пятизначное число:', num)
res = num % 10
sr_ar = res
num //= 10
res *= num % 10
sr_ar += num % 10
num //= 10
res *= num % 10
sr_ar += num % 10
num //= 10
res *= num % 10
sr_ar += num % 10
num //= 10
res *= num % 10
sr_ar += num % 10

print('Произведение цифр числа 97531:', res)
print('Среднее арифметическое:', sr_ar / 5)  # сразу на 5 потому что указано 5-значное число
