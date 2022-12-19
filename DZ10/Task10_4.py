"""
Створіть магазин канцтоварів використовуючи списки для зберігання елементів. Для додавання елементів створіть
функцію, яка буде запитувати дані в користувача і зібрані дані у вигляді кортежу додавати у створений список
на початку. Результат вивести на екран. Під час створення дотримуйтесь правил специфікації PEP 8.
"""
from typing import Tuple

my_list = ['Books', 'pencils', 'albums', 'notebooks', 'pens']



def add():
    my_ls = tuple(input('enter new item ').split(' '))
    my_list.insert(0, my_ls)
    return my_list


new_list = add()
print(new_list)
