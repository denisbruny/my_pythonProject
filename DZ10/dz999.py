"""

Створіть функцію, яка на вхід отримує цілочисельне значення й повертає рядок у розгорнутому вигляді:
1) 15 -> '10 + 5'           2) 63 -> '60 + 3'        3) 90925 -> '90000 + 900 + 20 + 5'

"""

z = input('enter number')
print(z, '= ', end='')
for i in range(len(z)):
    if i == len(z) - 1:
        print(z[i], end='')
    else:
        print(z[i] + ("0" * (len(z) - i - 1)) + '+', end='')



