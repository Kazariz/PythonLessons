total_area = 0


def parallelepiped_area(a, b, c):
    total_area_local = 0

    def rectangle_area(x, y):
        return x * y

    total_area_local = 2 * (rectangle_area(a, b) + rectangle_area(b, c) + rectangle_area(a, c))
    return total_area_local


def parallelepiped_area_nonlocal(a, b, c):
    total_area_nonlocal = 0

    def calculate():
        nonlocal total_area_nonlocal

        def rectangle_area(x, y):
            return x * y

        total_area_nonlocal = 2 * (rectangle_area(a, b) + rectangle_area(b, c) + rectangle_area(a, c))

    calculate()
    return total_area_nonlocal


print(parallelepiped_area(2, 4, 6))  # 88
print(parallelepiped_area_nonlocal(5, 8, 2))  # 132
print(parallelepiped_area_nonlocal(1, 6, 8))  # 124
