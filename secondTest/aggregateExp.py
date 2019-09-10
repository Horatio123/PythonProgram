class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

    def yearly_income(self):
        return self.pay * 12 + self.bonus


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.obj_salary = salary

    def yearly_salary(self):
        return self.obj_salary.yearly_income()


salary = Salary(10000, 16000)
employee = Employee('Alex', salary)
print(employee.yearly_salary())
