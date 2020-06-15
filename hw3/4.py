#!/usr/bin/python
# -*- coding: UTF-8 -*-

def sqr(a, n):
    result = 1
    for i in range(abs(n)):
        result *= a
    if n >= 0:
        return result
    else:
        return 1 / result

 
if __name__ == '__main__':
    print(sqr(float(input('Введите основание степени: ')), int(input('Введите полказатель степени: '))))