from abc import ABC
from abc import abstractmethod


class Shape(ABC):

    @abstractmethod
    def perimeter(self):

        """
        """

    @abstractmethod
    def area(self):

        """
        """


class Circle(Shape):

    def __init__(self,r):
        self.radius = r

    def area(self):
        return str(self.radius**2) + '\u03A0'

    def perimeter(self):
        return str(self.radius*2) + '\u03A0'


class Rectangle(Shape):

    def __init__(self, a, b):

        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return 2 * self.a + 2 * self.b


class Square(Shape):

    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4


K = Circle(3)
print(K.area())
print(K.perimeter())