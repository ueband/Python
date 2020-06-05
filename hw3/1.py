#!/usr/bin/python
# -*- coding: UTF-8 -*-

def div(*args):
    try:
        a = int(input("Введите делимое "))
        b = int(input("Введите делитель "))
        c = a / b
    except ValueError:
        return 'Вы не ввели число'
    except ZeroDivisionError:
        return "Ошибка! Вы не можете делить на '0'."
    return c
    
if __name__ == '__main__':
    print(f'Результат  {div()}')
