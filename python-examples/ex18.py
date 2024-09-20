class Person:
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.name = kwargs.get('name')
        self.email = kwargs.get('email')

    def print(self):
        print(f'Name  = {self.name}')
        print(f'Email = {self.email}')


class Employee(Person):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.empno = kwargs.get('empno')
        self.salary = kwargs.get('salary')

    def print(self):
        print(f'Empno = {self.empno}')
        super().print()
        print(f'Salary= ₹ {self.salary}')

def main():
    p1 = Employee(name='Vinod', email='vinod@vinod.co', empno=1122, salary=50_000)
    p1.print()
    print('='*60)
    Person.print(p1)
    # print(dir(p1))


if __name__ == '__main__':
    main()
    
