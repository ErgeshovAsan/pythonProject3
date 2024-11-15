class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length * self.__side_length

    def info(self):
        area_square = self.calculate_area()
        return f'Square side length: {self.__side_length}{Figure.unit}, area: {area_square}{Figure.unit}.'


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area_rectangle = self.calculate_area()
        return f'Rectangle length: {self.__length}{Figure.unit}, width: {self.__width}{Figure.unit},  area: {area_rectangle}{Figure.unit}.'


figures = [
    Square(5),
    Square(10),
    Rectangle(2, 3),
    Rectangle(4, 5),
    Rectangle(6, 7)
]

for figure in figures:
    print(figure.info())