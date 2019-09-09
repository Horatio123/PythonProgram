class Polygon:
    __width = None
    __height = None

    def set_value(self, width, height):
        self.__width = width
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height


class Rectangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width()


class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() / 2


rectangle = Rectangle()
rectangle.set_value(3, 4)
print(rectangle.area())

triangle = Triangle()
triangle.set_value(3, 4)
print(triangle.area())
