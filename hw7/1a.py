#!/usr/bin/python
# -*- coding: UTF-8 -*-

from copy import deepcopy

class Matrix:
    def __init__(self, list_of_lists):
        self.matrix = deepcopy(list_of_lists)

    def __str__(self):
        return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def size(self):
        sizepair = (len(self.matrix), len(self.matrix[0]))
        return sizepair

    def __getitem__(self, idx):
        return self.matrix[idx]

    def __add__(self, other):
        other.matrix = Matrix(other)
        result = []
        numbers = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                summa = other.matrix[i][j] + self.matrix[i][j]
                numbers.append(summa)
                if len(numbers) == len(self.matrix):
                    result.append(numbers)
                    numbers = []
        return Matrix(result)


mtr1 = Matrix([[10, 45, 15], [85, 12, 33], [4, 35, 1]])
mtr2 = Matrix([[45, 8, 3], [7, 24, 9], [2, 8, 17]])



print(mtr1+mtr2)
