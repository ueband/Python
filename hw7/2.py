#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Textil:
    def __init__(self, V, H):
        self.V = V
        self.H = H

    def get_consumption_c(self):
        return self.V / 6.5 + 0.5

    def get_consumption_j(self):
        return self.H * 2 + 0.3

    @property
    def get_consumption_full(self):
        return str(f'Общий расход ткани \n'
                   f' {(self.V / 6.5 + 0.5) + (self.H * 2 + 0.3)}')


class Coat(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.consumption_c = round(self.V / 6.5 + 0.5)

    def __str__(self):
        return f'Расход ткани на пальто {self.consumption_c}'


class Jacket(Textil):
    def __init__(self, V, H):
        super().__init__(V, H)
        self.consumption_j = round(self.H * 2 + 0.3)

    def __str__(self):
        return f'Расход ткани на костюм {self.consumption_j}'

coat = Coat(15, 5)
jacket = Jacket(3, 12)
print(coat)
print(jacket)
print(coat.get_consumption_full)
print(jacket.get_consumption_full)
print(jacket.get_consumption_c())
print(jacket.get_consumption_j())