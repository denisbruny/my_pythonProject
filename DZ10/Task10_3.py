"""Створіть інженерний калькулятор з використанням модуля math, в якому передбачене меню. Під час
створення дотримуйтесь правил специфікації PEP 8."""


import math


def summ(a, b):
    return a + b


def sub(a, b):
    return a - b


def mult(a, b):
    return a * b


def div(a, b):
    if b == 0:
        return 'Can`t divide by 0'
    else:
        return (a / b)


def add(a, b):
    return math.pow(a, b)



def sq(a):
    if a < 0:
        return 'X Negative meaning'
    else:
        return math.sqrt(a)


def cub(a):
    return math.pow(a, (1/3))


def sin(a):
    return math.sin(a)


def cos(a):
    return math.cos(a)


def tg(a):
    return math.tan(a)


while True:
    print('1. x+y       6. x √2')
    print('2. x-y       7. x √3')
    print('3. x*y       8. sin(x)')
    print('4. x/y       9. cos(x)')
    print('5. x^y      10. tg(x)')
    print('     11. exit')
    n = int(input('your choice '))
    if n == 1:
        a, b = map(float, input('enter x and y - by space').split(" "))
        print(a, '+', b, '=', summ(a, b), '\n')
    elif n == 2:
        a, b = map(float, input('enter x and y - by space').split(" "))
        print(a, '-', b, '=', sub(a, b), '\n')
    elif n == 3:
        a, b = map(float, input('enter x and y - by space').split(" "))
        print(a, '*', b, '=', mult(a, b), '\n')
    elif n == 4:
        a, b = map(float, input('enter x and y - by space').split(" "))
        ddd = div(a, b)
        print(a, '/', b, '=', ddd, '\n')
    elif n == 5:
        a, b = map(float, input('enter x and y - by space').split(" "))
        aaa = add(a, b)
        print(a, '^', b, '=', aaa, '\n')
    elif n == 6:
        a = float(input('enter number'))
        nnn = sq(a)
        print('2√', a, '=', nnn, '\n')
    elif n == 7:
        a = float(input('enter number'))
        print('3√', a, '=', cub(a), '\n')
    elif n == 8:
        a = float(input('enter number'))
        print('sin(', a, ')=', sin(a), '\n')
    elif n == 9:
        a = float(input('enter number'))
        print('cos(', a, ')=', cos(a), '\n')
    elif n == 10:
        a = float(input('enter number'))
        print('tg(', a, ')=', tg(a), '\n')
    elif n == 11:
        break
    else:
        continue