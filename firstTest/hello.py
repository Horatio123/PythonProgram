print ("hello python world")


class Student:
    pass


student1 = Student()

print (student1)

student1.name = "horatio"
print (student1.name)


class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@baimahu.com'

    def fullname(self):
        return '{}, {}'.format(self.first, self.last)


employee1 = Employee("Alex", "Jobs", 5000)
print (employee1.email)
print ('{}, {}'.format(employee1.first, employee1.last))
print employee1.fullname()
print Employee.fullname(employee1)
