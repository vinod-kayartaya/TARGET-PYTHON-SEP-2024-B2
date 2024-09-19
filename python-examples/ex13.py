class Car(object):
    def __init__(self, make=None, model=None, color=None) -> None:
        # python runtime invokes this method automatically when an object is created,
        # and passes the reference of the newly constructed object in the heap, along with
        # any additional parameters supplied by the user
        self.make = make
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return f'Car object with make={self.make}, model={self.model} and color={self.color}'


def main():
    c1 = Car('Honda', 'City', 'Red')  # in Java -->  `Car c1 = new Car();`
    c2 = Car('Hyundai', color='Red', model='i10')

    print(f'{c1.make = }')
    print(f'{c1.model = }')
    print(f'{c1.color = }')

    print(f'{c2.make = }')
    print(f'{c2.model = }')
    print(f'{c2.color = }')

    print(c1)  # print(c1.__str__())
    print(c2)


if __name__ == '__main__':
    main()
    
