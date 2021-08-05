class Cell:

    def __init__(self, data):
        self.data = int(data)

    def __add__(self, other):
        return f'Сложение: {self.data + other.data}'

    def __sub__(self, other):
        sub = self.data - other.data
        return f'Вычитание: {self.data - other.data}' if sub > 0 else 'Разность количества ячеек двух клеток меньше нуля!!!!!!'

    def __truediv__(self, other):
        return f'Деление: {self.data // other.data}'

    def __mul__(self, other):
        return f'Умножение: {self.data * other.data}'

    def make_order(self, data2):
        result = ''
        for x in range(self.data // data2):
            result += '*' * data2 + '\n'
        result += '*' * (self.data - (data2 * (self.data // data2)))
        return result


cell = Cell(15)
cell_2 = Cell(8)
print(cell + cell_2)
print(cell - cell_2)
print(cell / cell_2)
print(cell * cell_2)
print(cell.make_order(6))
