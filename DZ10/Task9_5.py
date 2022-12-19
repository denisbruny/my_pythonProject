"""
Створіть функцію quadratic_equation, яка приймає на вхід 3 параметри: a, b, c. Усередині цієї функції
створити змінні x1, x2 зі значенням None (спочатку приймаємо, що рівняння не має коренів) та функцію
calc_rezult з формальними параметрами зовнішньої функції quadratic_equation. Всередині функції calc_rezult
здійснити пошук дискримінанта, згідно з результатом якого зробити розрахунок коренів рівняння. Зовнішня
функція quadratic_equation має повернути перелік значень коренів квадратного рівняння. Надати можливість
користувачеві ввести з клавіатури формальні параметри для передачі їх у створену функцію quadratic_equation,
результати роботи функції відобразити на екрані.
"""


def quadratic_equation(a, b, c):
    x1 = 'none'
    x2 = 'none'

    def calc_res(a, b, c):
        d = float(b ** 2 - (4 * a * c))
        if d < 0:
            x1 = 'no roots'
            x2 = 'no roots'
        elif d == 0:
            x1 = float((-b) / 2 ** a)
            x2 = float((-b) / 2 ** a)
        else:
            x1 = float((-b + (d ** (1 / 2))) / (2 * a))
            x2 = float((-b - (d ** (1 / 2))) / (2 * a))
        return x1, x2

    q2 = calc_res(a1, b1, c1)
    x1 = q2[0]
    x2 = q2[1]
    return x1, x2


a1, b1, c1 = map(float, input('enter a b c').split(' '))
summ = quadratic_equation(a1, b1, c1)
print('x1 =', summ[0], ' x2 =', summ[1])
