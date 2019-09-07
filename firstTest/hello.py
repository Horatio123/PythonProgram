print ("hello python world")


class Student:
    pass


student1 = Student()

print (student1)

student1.name = "horatio"
print (student1.name)


class Employee:
    def __init__(self, first='Tom', last='Gates', pay=1000):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@baimahu.com'

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)


employee1 = Employee("Alex", "Jobs", 5000)
employee2 = Employee()
employee3 = Employee('Jerry')
print (employee1.email)
print ('{}, {}'.format(employee1.first, employee1.last))
print employee1.fullname()
print employee2.fullname()
print employee3.fullname()
print Employee.fullname(employee1)


def fun(*args, **kwargs):
    for arg in args:
        print arg

    for item in kwargs.items():
        print item


print fun('pig', 'dog', name='Tom')

# class Company:
#     def __init__(self, *args, **kwargs):
#
#     def fullname(self):
#         for arg in self:
#             print arg
#
#
# company1 = Company('name', 'location', name='xiao')
# print company1.fullname()
