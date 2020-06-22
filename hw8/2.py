#!/usr/bin/python
# -*- coding: UTF-8 -*-

class DivisionByNull:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    @staticmethod
    def divide_by_null(dividend, divisor):
        try:
            return (dividend / divisor)
        except:
            return (f"Деление на ноль запрещено")


div = DivisionByNull(1, 5)
print(DivisionByNull.divide_by_null(25, 0))
print(DivisionByNull.divide_by_null(2, 0.5))
print(div.divide_by_null(50, 0.0))
