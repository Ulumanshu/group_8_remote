from math import pow, sqrt
import matplotlib.pyplot as plt


class AbstractFigure:
    __count = 0
    plot = plt

    def __init__(self, plotter):
        AbstractFigure.__count += 1
        self.id = AbstractFigure.__count
        self.plot = plotter

    def draw_line(self, x_values, y_values, color):
        self.plot.plot(x_values, y_values, linewidth=0.25, color=color)

    def draw_dot(self, x, y, color):
        self.plot.plot([x], [y], marker='o', markersize=3, color=color)

    def draw_circle(self, x, y, radius, color):
        circle = self.plot.Circle((x, y), radius, color=color)
        self.plot.gca().add_patch(circle)

    @classmethod
    def how_many_figures(cls):
        return cls.__count

    @classmethod
    def plot_all(cls):
        cls.plot.show()


class Dot(AbstractFigure):
    def __init__(self, coordinates, color="red"):
        super(Dot, self).__init__(plt)
        self.coordinates = coordinates
        self.center = coordinates[0]
        self.color = color

    def __repr__(self):
        return f"Dot id: {self.id}, center: {self.center}"

    def perimeter(self):
        return 0

    def plot_me(self):
        self.draw_dot(self.center[0], self.center[1], self.color)


class Circle(AbstractFigure):
    def __init__(self, coordinates, radius=1, color="red"):
        super(Circle, self).__init__(plt)
        self.coordinates = coordinates
        self.center = coordinates[0]
        self.radius = radius
        self.color = color

    def __repr__(self):
        return f"Radius id: {self.id}, center: {self.center}"

    def perimeter(self):
        return 0

    def plot_me(self):
        self.draw_circle(self.center[0], self.center[1], self.radius, self.color)


class Line(AbstractFigure):
    def __init__(self, coordinates, color="red"):
        super(Line, self).__init__(plt)
        self.coordinates = coordinates
        self.check_valid(self.coordinates)
        self.length = self.calculate_length()
        self.center = coordinates[0]
        self.color = color

    def __repr__(self):
        return f"Line id: {self.id}, center: {self.center}"

    def perimeter(self):
        return self.calculate_length()

    def plot_me(self):
        x_values = [self.coordinates[0][0], self.coordinates[1][0]]
        y_values = [self.coordinates[0][1], self.coordinates[1][1]]
        self.draw_line(x_values, y_values, self.color)

    @classmethod
    def check_valid(cls, coordinates):
        if len(coordinates) != 2:
            raise ValueError(f'Line must have 2 points :{coordinates}')

    def calculate_length(self):
        point_1 = self.coordinates[0]
        point_2 = self.coordinates[1]
        return sqrt(pow(point_2[0] - point_1[0], 2) + pow(point_2[1] - point_1[1], 2))


class Triangle(AbstractFigure):
    def __init__(self, coordinates, color="black"):
        super(Triangle, self).__init__(plt)
        self.coordinates = coordinates
        self.check_valid(self.coordinates)
        self.color = color
        self.lines = []
        self.create_figure_lines()
        # self.length = self.calculate_length()
        # self.center = coordinates[0]

    def __repr__(self):
        return f"Trikampis id: {self.id}, Coordinates: {self.coordinates}"

    def create_figure_lines(self):
        for i in range(len(self.coordinates)):
            line_coordinates = self.coordinates[i:i + 2]
            if len(line_coordinates) == 1:
                line_coordinates = [line_coordinates[0], self.coordinates[0]]
            print(line_coordinates)
            line_object = Line(line_coordinates, self.color)
            self.lines.append(line_object)

    def perimeter(self):
        return sum([line.length for line in self.lines])

    def plot_me(self):
        for line in self.lines:
            line.plot_me()

    @classmethod
    def check_valid(cls, coordinates):
        if len(coordinates) != 3:
            raise ValueError(f'Triangle must have 3 points :{coordinates}')

# Sutvarkyti Rectangle taip kaip sutvarkytas Triangle, kad jis sudarytu 4 line objektai, veiktu perimetras etc.
# Sutvarkyti klases Circle perimetro funcija
# Kiti daugiakampiai

# Kokia kita funcija pvz sinusoida # sunku


class Rectangle(AbstractFigure):
    def __init__(self, a=(0, 0), b=(0, 1), c=(1, 0), d=(1, 1), colour='red'):
        super(Rectangle, self).__init__(plt)
        self.colour = colour
        self.point_1 = a
        self.point_2 = b
        self.point_3 = c
        self.point_4 = d
        print(self.point_1, self.point_2, self.point_3, self.point_4)
        self.l1 = sqrt(pow(self.point_1[0] - self.point_2[0], 2) + pow(self.point_2[1] - self.point_1[1], 2))
        self.l2 = sqrt(pow(self.point_3[0] - self.point_2[0], 2) + pow(self.point_3[1] - self.point_2[1], 2))
        self.l3 = sqrt(pow(self.point_4[0] - self.point_3[0], 2) + pow(self.point_4[1] - self.point_3[1], 2))
        self.l4 = sqrt(pow(self.point_1[0] - self.point_4[0], 2) + pow(self.point_1[1] - self.point_4[1], 2))
        self.check_valid(self.l1, self.l2, self.l3, self.l4)

    def __repr__(self):
        return f"Kvadratas A: {self.point_1}, B: {self.point_2}, C: {self.point_3}, D: {self.point_4}"

    def perimeter(self):
        return self.l1 + self.l2 + self.l3 + self.l4

    @classmethod
    def check_valid(cls, l1, l2, l3, l4):
        if l1 != l3:
            raise ValueError(f'l1:{l1} nelygu l3:{l3}')
        if l2 != l4:
            raise ValueError(f'l2:{l2} nelygu l4:{l4}')

    def plot_me(self):
        l1_x_values = [self.point_1[0], self.point_2[0]]
        l1_y_values = [self.point_1[1], self.point_2[1]]
        self.draw_line(l1_x_values, l1_y_values, self.colour)
        l2_x_values = [self.point_2[0], self.point_3[0]]
        l2_y_values = [self.point_2[1], self.point_3[1]]
        self.draw_line(l2_x_values, l2_y_values, self.colour)
        l3_x_values = [self.point_3[0], self.point_4[0]]
        l3_y_values = [self.point_3[1], self.point_4[1]]
        self.draw_line(l3_x_values, l3_y_values, self.colour)
        l4_x_values = [self.point_4[0], self.point_1[0]]
        l4_y_values = [self.point_4[1], self.point_1[1]]
        self.draw_line(l4_x_values, l4_y_values, self.colour)


class FigureFactory:
    def __init__(self, input_data):
        self.coordinates_list = input_data[0]
        self.color = input_data[1]
        self.radius = len(input_data) > 2 and input_data[2] or 0
        self.figure_object = False
        self.choose_figure()

    def choose_figure(self):
        if len(self.coordinates_list) == 1:
            if self.radius:
                self.figure_object = Circle(self.coordinates_list, self.radius, self.color)
            else:
                self.figure_object = Dot(self.coordinates_list, self.color)
        elif len(self.coordinates_list) == 2:
            self.figure_object = Line(self.coordinates_list, self.color)
        elif len(self.coordinates_list) == 3:
            self.figure_object = Triangle(self.coordinates_list, self.color)
        elif len(self.coordinates_list) == 4:
            self.figure_object = Rectangle(*self.coordinates_list, self.color)


if __name__ == "__main__":
    # triangle_data = [
    # ((1, 2), (1, 6), (2, 4)),
    # ((2, 3), (2, 7), (3, 5)),
    # ((3, 4), (3, 8), (8, 6)),
    # ]
    # square_data = [
    # ((1, 2), (1, 6), (6, 6), (6, 2), 'blue'),
    # ((1, 2), (1, 3), (3, 3), (3, 2), 'green'),
    # ((1, 1), (1, 8), (4, 8), (4, 1), 'red'),
    # ]

    figure_data = [
        ([(1, 2)], 'blue', 5),
        ([(3, 3)], 'red'),
        ([(4, 8)], 'yellow', 2),
        ([(10, 10)], 'magenta'),
        ([(1, 2), (3, 4)], 'black'),
        ([(3, 3), (3, 7)], 'black'),
        ([(4, 8), (8, 12)], 'black'),
        ([(10, 10), (4, 8)], 'black'),
        ([(1, 2), (1, 6), (2, 4)], 'black'),
        ([(1, 2), (1, 6), (6, 6), (6, 2)], 'red'),
    ]

    figure_list = []
    for figure in figure_data:
        abs_figure_object = FigureFactory(figure)
        abs_figure_object.figure_object.plot_me()
        figure_list.append(abs_figure_object)
        print(type(abs_figure_object.figure_object), abs_figure_object.figure_object.perimeter())

    first_figure = figure_list[0]
    first_figure.figure_object.plot_all()
