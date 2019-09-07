class School:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name


chunhui = School('chunhui', 110)

print chunhui.get_name()
print chunhui.set_name('chunwai')
print chunhui.get_name()
