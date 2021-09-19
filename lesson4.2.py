# 2: Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def get_max(a, b, c):
    result = max([a, b, c])
    return result


result = get_max(1, 5, 11)
print(result)
