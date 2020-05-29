#!/usr/bin/python
# -*- coding: UTF-8 -*-

digit = input('Введите число ')
print('Вы ввели: ' + digit)
digit_2 = int(digit + digit)
digit_3 = int(digit + digit + digit)
digit = int(digit)
final = digit + digit_2 + digit_3
print(f'Результат:  {digit} + {digit_2} + {digit_3} = {final}')

