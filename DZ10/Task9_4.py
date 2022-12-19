"""
Напишіть рекурсивну функцію, яка обчислює суму натуральних чисел, які входять до заданого проміжку.
"""


def totalsumm(a, b):
    if a == b:
        return 1
    else:
        return b + totalsumm(a, b - 1)


n, m = map(int, input('Enter a range of numbers - by space').split(' '))
print('Sum of numbers =', totalsumm(n, m))
