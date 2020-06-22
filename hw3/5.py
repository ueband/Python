#!/usr/bin/python
# -*- coding: UTF-8 -*-

def my_f ():
    s_result = 0
    ext = False
    while ext == False:
        number = input('Введите число или "Q" для выхода из программы - ').split()

        result = 0
        for i in range(len(number)):
            up = number[i]
            up = up.upper()
            if up == 'Q':
                ext = True
                break
            else:
                result = result + int(number[i])
        s_result = s_result + result
        print(f'Current sum is {s_result}')
    print(f'Your final sum is {s_result}')

if __name__ == '__main__':
    my_f() 