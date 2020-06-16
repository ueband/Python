#!/usr/bin/python
# -*- coding: UTF-8 -*-
lst = [9, 5, 3, 1]
print(f'Рейтинг  {lst}')
dgt = int(input('Введите число: '))
while dgt != 666:
    for i in range(len(lst)):
        if lst[i] == dgt:
            lst.insert(i + 1, dgt)
            break
        elif lst[i] > dgt and lst[i + 1] < dgt:
            lst.insert(i + 1, dgt)
            break
        elif lst[0] < dgt:
            lst.insert(0, dgt)
        elif lst[-1] > dgt:
            lst.append(dgt)
    print(f"текущий список - {lst}")
    dgt = int(input('Введите число: '))
print("Досвидания")
