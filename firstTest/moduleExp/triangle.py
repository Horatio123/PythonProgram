from polygon import Polygon


class Triangle(Polygon):
    def area(self):
        return self.get_height() * self.get_width() / 2
