#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Error:
    def __init__(self, *args):
        self.lst = []

    def my_input(self):
        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.lst.append(val)
                
                print(f'Текущий список - {self.lst} \n ')
            except:
                print(f"Недопустимое значение. Разрешен ввод")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(test.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Досвидания'
                else:
                    return f'Досвидания'

test = Error()
print(test.my_input())
