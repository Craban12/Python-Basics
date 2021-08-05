import numpy


class Matrix:
    def __init__(self, data_matrix):
        self.res_matrix = numpy.array(data_matrix)

    def __add__(self, other):
        return Matrix(self.res_matrix + other.res_matrix)

    def __str__(self):
        return f"{self.res_matrix}"


M_1 = Matrix([[1, 2, 3], [3, 2, 1]])
M_2 = Matrix([[4, 5, 6], [6, 5, 4]])

print(M_1 + M_2)
