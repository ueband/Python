#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Road:
    _length = None
    _width = None
    weigth = None
    tickness = None
    def __init__(self, length, width):
        self.length = length
        self.width = width
        print('To create a road,')

    def need(self):
        self.weigth = 0.025
        self.tickness = 0.05
        need = self.length * self.width * self.weigth * self.tickness
        print(f'you will need {need} ton asphalt')

road = Road(20, 5000)
road.need()