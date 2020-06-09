#!/usr/bin/python
# -*- coding: UTF-8 -*-

time = input('Введите время в секундах: ')
print('Вы ввели: ' + time)
time = int(time)
hh = time//3600
mm = time//60 - 60*hh
ss = time%60
print(f'Результат (чч:мм:сс) {hh}:{mm}:{ss}')
