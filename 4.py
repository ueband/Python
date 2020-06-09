#!/usr/bin/python
# -*- coding: UTF-8 -*-

digit = input('Введите целое положительное число: ')
print('Вы ввели: ' + digit)
temp = 0
digit = int(digit)
while digit > 0:
    d0 = digit%10
    digit = digit//10
    if temp < d0: 
        temp = d0
    
print(f'Наибольшая цифра:  {temp}')
  