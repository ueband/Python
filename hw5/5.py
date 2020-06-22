#!/usr/bin/python
# -*- coding: UTF-8 -*-

try:
    with open('5.txt', 'w') as f:
        line = input('Введите цифры через пробел \n')
        f.writelines(line)
        numbers = line.split()

        print(sum(map(int, numbers)))
except IOError:
    print('Ошибка чтения/записи файла')
except ValueError:
    print('Вы ввели не цифровое значение')
