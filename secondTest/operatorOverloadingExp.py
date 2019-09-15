class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def area(self):
        return self.__radius ** 2

    def __add__(self, other):
        return Circle(self.__radius + other.__radius)

    def __str__(self):
        return "circle ares is: " + str(self.area())

    def __gt__(self, other):
        return self.__radius > other.__radius


circle1 = Circle(3)
circle2 = Circle(4)
print("circle1's area is: ", circle1)
circle3 = circle1 + circle2
print("circle3's area is: ", circle3)
print(circle2 > circle1)
