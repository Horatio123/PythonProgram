class School:
    def __init__(self, name, year):
        self.__name = name
        self.__year = year

    def set_name(self, value):
        self.__name = value

    def get_name(self):
        return self.__name

    def print_name(self):
        print 'public method:'
        print self.__name
        self.__print_private()

    def __print_private(self):
        print 'private method:'
        print self.__year


chunhui = School('chunhui', 110)

print chunhui.get_name()
chunhui.set_name('chunwai')
print chunhui.get_name()
chunhui.print_name()
chunhui
