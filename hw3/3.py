#!/usr/bin/python
# -*- coding: UTF-8 -*-

def my_func(a , b, c):
    m = min(a, b, c)
    result = a + b + c -m
    return result

if __name__ == '__main__':
    print(my_func(2, 5, 1))