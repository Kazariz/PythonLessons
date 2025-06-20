def average_decorator(func):
    def wrapper(*args):
        total = func(*args)
        avg = total / len(args)
        print(f"Среднее арифметическое чисел {', '.join(map(str, args))} = {avg}")
        return total

    return wrapper


@average_decorator
def sum_numbers(*args):
    total = sum(args)
    print(f"Сумма чисел {', '.join(map(str, args))} = {total}")
    return total


sum_numbers(2, 3, 3, 4)
