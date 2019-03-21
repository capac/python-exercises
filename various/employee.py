import datetime


class Employee:
    '''Template for company employee'''
    raise_amt = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def __repr__(self):
        return f'Employee({self.first}, {self.last}, {self.pay})'

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @staticmethod
    def is_workday(date):
        if date.weekday == 5 or date.weekday == 6:
            return False
        return True


class Developer(Employee):
    '''Template for company developer, modelled on company employee'''
    raise_amt = 1.1

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

    def __repr__(self):
        return f'Developer({self.first}, {self.last}, {self.pay}, {self.prog_lang})'


if __name__ == '__main__':
    emp_1 = Employee('Sue', 'Mitchell', 70000)
    print(emp_1)
    date = datetime.date(2019, 3, 14)
    print(Employee.is_workday(date))
    emp_2 = Developer('Patricia', 'Hopkins', 55000, ['Ruby', 'C#'])
    Developer.raise_amt = 1.2
    emp_2.apply_raise()
    print(emp_2)
