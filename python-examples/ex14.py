from typing import Any


class Laptop:
    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.model = kwargs.get('model')
        self.price = kwargs.get('price')

    # this is a function representing the getter property `make` (readable property or accessor)
    @property
    def make(self) -> str:
        return self.__make
    
    # this is a function representing the setter property `make` (aka writable property or mutator)
    @make.setter
    def make(self, value) -> None:
        if value is not None and type(value) != str:
            raise TypeError('`make` must be a str')
        
        self.__make = value

    @property
    def model(self) -> str:
        return None if self.__model is None else self.__model.upper()
    
    @model.setter
    def model(self, value) -> None:
        if value is not None and type(value) != str:
            raise TypeError('`model` must be a str')
        
        self.__model = value

    @property
    def price(self) -> str:
        return self.__price
    
    @price.setter
    def price(self, value) -> None:
        if value is not None and type(value) not in (int, float):
            raise TypeError('`price` must be a number')
        
        if value is not None and value < 0:
            raise ValueError('`price` must be >= 0')
        
        self.__price = value

    def __str__(self) -> str:
        return f'Laptop object with make="{self.make}", model="{self.model}", price={self.price}'
    
    def print(self) -> None:
        print('Laptop details:')
        print(f'Make   = {self.make}')
        print(f'Model  = {self.model}')
        print(f'Price  = ₹ {0 if self.price is None else self.price}')
        print()


def main():
    l1 = Laptop(make='Apple', model='macbook pro', price=180_000)
    l2 = Laptop(make='HP', model='pavilion', price=72_000)

    print(l1)
    print(l2)
    l1.print()  # Laptop.print(l1)
    l2.print()  # Laptop.print(l2)

if __name__ == '__main__':
    main()
