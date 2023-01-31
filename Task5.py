"""
5. Сделайте профилирование кода любого или любых выполненных заданий
с помощью модуля timeit, опишите результат
"""

from timeit import timeit


def my_func1(num1, num2, num3):
    lst = []
    lst.extend([num1, num2, num3])
    lst.sort()
    return lst[-1] + lst[-2]


def my_func2(num1, num2, num3):
    lst = []
    lst.extend([num1, num2, num3])
    max1 = max(lst)
    lst.remove(max1)
    return max1 + max(lst)


n1 = int(input('Введите число 1: '))
n2 = int(input('Введите число 2: '))
n3 = int(input('Введите число 3: '))

print('Производительность функций при повторении 10000 раз')
print('my_func1 (с функцией sort):', timeit(
    "my_func1(n1, n2, n3)", globals=globals(), number=10000))
print('my_func2 (без функциеи sort):', timeit(
    "my_func2(n1, n2, n3)", globals=globals(), number=10000))
