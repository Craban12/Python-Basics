class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.standart = 25
        self.thickness = 5

    def mass(self):
        mass_result = self._length * self._width * self.standart * self.thickness
        print(mass_result)


x = Road(100, 6)
x.mass()
