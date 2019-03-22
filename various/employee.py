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
    raise_amt = 1.06

    def __init__(self, first, last, pay, prog_lang=None):
        super().__init__(first, last, pay)
        if prog_lang is None:
            self.prog_lang = []
        else:
            self.prog_lang = [prog_lang]

    def __repr__(self):
        prog_lang = self.prog_lang[0] if len(self.prog_lang) == 1 else self.prog_lang
        return f'Developer({self.first}, {self.last}, {self.pay}, {prog_lang})'

    def add_lang(self, progs):
        for prog in progs:
            if prog not in self.prog_lang:
                self.prog_lang.append(prog)

    def remove_lang(self, progs):
        for prog in progs:
            if prog in self.prog_lang:
                self.prog_lang.remove(prog)


if __name__ == '__main__':
    emp_1 = Employee('Sue', 'Mitchell', 70000)
    print('Employee 1:', emp_1)
    date = datetime.date(2019, 3, 14)
    print(Employee.is_workday(date))
    emp_2 = Developer('Patricia', 'Hopkins', 55000, 'C++')
    print('Employee 2:', emp_2)
    Developer.raise_amt = 1.08
    emp_2.apply_raise()
    emp_2.add_lang(['Python', 'JavaScript'])
    print('Employee 2:', emp_2)
    emp_2.remove_lang(['C#', 'Ruby', 'Bash'])
    print(emp_2)
