import math

class Figure:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self): #Nesupratau salygos, atrode, kad reikia metodu visose klasese, net 'parent'
        area = self.width * self.length
        return f'Your figure area is: {area}'

    def perimeter(self): #Nesupratau salygos, atrode, kad reikia metodu visose klasese, net 'parent'
        perimeter = (self.width + self.length) * 2
        return f'Your figure perimeter is {perimeter}'
class Rectangle(Figure):

    def calculate_area(self):
        area = self.width * self.length
        return f'Your Rectangle area is: {area}'
    def calculate_perimeter(self):
        perimeter = (self.width + self.length) * 2
        return f'Your Rectangle perimeter is {perimeter}'
class RightTriangle(Figure):

    def calculate_s(self):
        s = int(self.width * self.length / 2)
        return f'Your Triangle area is {s}'

    def calculate_p(self):
        c = math.sqrt(self.length **2 + self.width **2)
        p = int(self.length + self.width + c)
        return f'Your Triangle perimeter is is {p}'

fig1 = Figure(4, 2)
rectangle = Rectangle(5, 10)
triangle = RightTriangle(3, 4)

print("Rectangle Information:")
print(rectangle.perimeter())
print(rectangle.calculate_perimeter())
print("Right Triangle Information:")
print(rectangle.area())
print(rectangle.calculate_area())
print(triangle.calculate_p())
print(triangle.calculate_s())
