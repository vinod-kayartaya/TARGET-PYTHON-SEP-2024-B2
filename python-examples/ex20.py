from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def dimensions(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius=1.0) -> None:
        super().__init__()
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2 

    @property
    def name(self):
        return 'circle'

    @property
    def dimensions(self):
        return f'radius={self.radius}'

class Rectangle(Shape):
    def __init__(self, width=1.0, height=1.0) -> None:
        super().__init__()
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def name(self):
        return 'rectangle'

    @property
    def dimensions(self):
        return f'width={self.width}, height={self.height}'
    
class Triangle(Shape):
    def __init__(self, base=1.0, height=1.0) -> None:
        super().__init__()
        self.base = base
        self.height = height

    @property
    def area(self):
        return 0.5 * self.base * self.height
    
    @property
    def name(self):
        return 'triangle'

    @property
    def dimensions(self):
        return f'base={self.base}, height={self.height}'
    

# polymorphic method
# the method accept objects of Shape (kind of an interface here)
# and the behavior of the method is based on the actual object that is received (like Circle, Triangle, etc)
def print_shape_details(shape: Shape) -> None:
    if not isinstance(shape, Shape):
        raise TypeError('Invalid type of parameter supplied. Must be Shape object.')
    
    print(f'Got an object of {shape.name}')
    print(f'area of the {shape.name} with dimensions of {shape.dimensions} is {shape.area}')
    print()


def main():
    c1 = Circle(1.2)
    r1 = Rectangle(1.2, 3.4)
    t1 = Triangle(1.2, 3.4)

    print_shape_details(c1)
    print_shape_details(r1)
    print_shape_details(t1)


if __name__ == '__main__':
    main()
    
