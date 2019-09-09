class Parent:
    def __init__(self, name):
        print('parent init', name)


class Parent2:
    def __init__(self):
        print('parent2 int')


class Child(Parent, Parent2):
    def __init__(self):
        print('child init')
        super().__init__('Tom')
        Parent.__init__(self, 'Jerry')
        Parent2.__init__(self)


child = Child()
print(Child.__mro__)
